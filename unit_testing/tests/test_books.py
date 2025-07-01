import unittest
import os
from unittest.mock import patch, MagicMock
import requests
import requests_mock
from bs4 import BeautifulSoup
from project.books import create_session, find_content, get_single_page_content, process_pages, get_chapter_content


class TestBooksFunctions(unittest.TestCase):

    def setUp(self):
        """创建测试用的session"""
        self.session = create_session()

        # 创建测试用的HTML内容
        self.simple_html = """
        <html>
            <body>
                <div id="content">测试内容</div>
                <div class="article">文章内容</div>
            </body>
        </html>
        """

        # 分页测试内容
        self.pagination_html = """
        <html>
            <body>
                <div id="htmlContent">第一页内容</div>
                <a href="/next_page">下一页</a>
            </body>
        </html>
        """

        self.next_page_html = """
        <html>
            <body>
                <div id="htmlContent">第二页内容</div>
            </body>
        </html>
        """

    def test_create_session(self):
        """测试创建带重试机制的session"""
        session = create_session()
        self.assertIsInstance(session, requests.Session)
        self.assertEqual(session.adapters['http://'].max_retries.total, 3)

    def test_find_content(self):
        """测试内容查找功能"""
        soup = BeautifulSoup(self.simple_html, 'html.parser')

        # 测试找到内容的情况
        selectors = ['#content', '.article']
        result = find_content(soup, selectors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "测试内容")

        # 测试找不到内容的情况
        selectors = ['#not-exist']
        result = find_content(soup, selectors)
        self.assertEqual(result, [])

        # 测试多个选择器的情况
        selectors = ['#not-exist', '.article']
        result = find_content(soup, selectors)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "文章内容")

    @requests_mock.Mocker()
    def test_get_single_page_content(self, mock):
        """测试获取单个页面内容"""
        # 模拟成功的请求
        mock.get('http://test.com/success', text=self.simple_html)
        soup, content = get_single_page_content('http://test.com/success',
                                                ['#content'], self.session)
        self.assertIsNotNone(soup)
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0].text, "测试内容")

        # 模拟失败的请求
        mock.get('http://test.com/fail', status_code=404)
        soup, content = get_single_page_content('http://test.com/fail',
                                                ['#content'], self.session)
        self.assertIsNone(soup)
        self.assertIsNone(content)

        # 模拟超时情况
        mock.get('http://test.com/timeout', exc=requests.exceptions.Timeout)
        soup, content = get_single_page_content('http://test.com/timeout',
                                                ['#content'], self.session)
        self.assertIsNone(soup)
        self.assertIsNone(content)

    @patch('project.books.get_single_page_content')
    def test_process_pages(self, mock_get_page):
        """测试分页处理功能"""
        # 设置模拟返回值
        mock_get_page.side_effect = [
            (BeautifulSoup(self.pagination_html, 'html.parser'), [
                BeautifulSoup('<div id="htmlContent">第一页内容</div>',
                              'html.parser')
            ]),
            (BeautifulSoup(self.next_page_html, 'html.parser'), [
                BeautifulSoup('<div id="htmlContent">第二页内容</div>',
                              'html.parser')
            ]),
            (None, None)  # 模拟找不到下一页
        ]

        # 执行测试
        result = process_pages('http://test.com/page1', ['#htmlContent'],
                               self.session)

        # 验证结果
        self.assertIn("第一页内容", result)
        self.assertIn("第二页内容", result)
        self.assertEqual(mock_get_page.call_count, 2)

        # 测试最大分页限制
        # 重置mock
        mock_get_page.side_effect = None
        mock_get_page.return_value = (BeautifulSoup(
            self.pagination_html, 'html.parser'), [
                BeautifulSoup('<div id="htmlContent">内容</div>', 'html.parser')
            ])

        # 执行测试（应该只运行2次）
        result = process_pages('http://test.com/page1', ['#htmlContent'],
                               self.session)
        self.assertEqual(result.count("内容"), 2)

    @patch('project.books.process_pages')
    @patch('project.books.get_single_page_content')
    def test_get_chapter_content(self, mock_get_page, mock_process_pages):
        """测试获取章节内容"""
        # 测试不需要分页的情况
        mock_get_page.return_value = (BeautifulSoup(
            '<html><body><div id="content">内容</div></body></html>',
            'html.parser'), [
                BeautifulSoup('<div id="content">内容</div>', 'html.parser')
            ])
        result = get_chapter_content('http://test.com/chapter', ['#content'],
                                     self.session)
        self.assertEqual(result, "内容")

        # 测试需要分页的情况
        # 使用更完整的HTML结构来触发分页检测
        page_html = """
        <html>
            <body>
                <div id="content">第一页内容</div>
                <a class="next-page" href="/next">下一页</a>
            </body>
        </html>
        """
        mock_get_page.return_value = (
            BeautifulSoup(page_html, 'html.parser'),
            [BeautifulSoup('<div id="content">第一页内容</div>', 'html.parser')]
        )
        mock_process_pages.return_value = "分页内容"
        result = get_chapter_content('http://test.com/chapter', ['#content'], self.session)
        self.assertEqual(result, "分页内容")

        # 测试获取失败的情况

        mock_get_page.return_value = (None, None)
        result = get_chapter_content('http://test.com/chapter', ['#content'],
                                    self.session)
        self.assertEqual(result, "[内容获取失败]")

        # 测试分页检测失败的情况
        mock_get_page.return_value = (BeautifulSoup(
            '<html><body><div>无分页内容</div></body></html>',
            'html.parser'), [BeautifulSoup('<div>无分页内容</div>', 'html.parser')])
        result = get_chapter_content('http://test.com/chapter', ['#content'],
                                    self.session)
        self.assertEqual(result, "无分页内容")

    def test_getValueList_with_invalid_url(self):

        """测试getValueList函数的invalid_urln处理"""
        from project.books import getValueList

        result = getValueList("not_a_valid_url", ['#content'], self.session)
        self.assertIsNone(result)

    def test_general_exception(self):

        """测试未预期的通用异常"""
        from project.books import getValueList

        self.session.get.side_effect = Exception("未预期的错误")
        result = getValueList(self.url, self.selector_list, self.session)
        self.assertIsNone(result)

    @patch('project.books.saveFile')
    @patch('project.books.getAllValue')
    @patch('project.books.getValueList')
    def test_main(self, mock_get_value_list, mock_get_all_value,
                  mock_save_file):
        """测试主函数"""
        from project.books import main

        # 设置模拟返回值
        mock_get_value_list.return_value = [
            MagicMock(text="章节1", href="chap1"),
            MagicMock(text="章节2", href="chap2")
        ]
        mock_get_all_value.return_value = "所有章节内容"

        # 执行主函数
        main()

        # 验证函数调用
        mock_get_value_list.assert_called_once()
        mock_get_all_value.assert_called_once()
        mock_save_file.assert_called_once_with("健身教练！.txt", "所有章节内容")

    def test_save_file(self):
        """测试文件保存功能"""
        from project.books import saveFile

        # 创建临时文件
        test_file = "test_output.txt"
        test_content = "测试内容"

        # 保存文件
        saveFile(test_file, test_content)

        # 验证文件内容
        with open(test_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertEqual(content, test_content)

        # 清理
        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
