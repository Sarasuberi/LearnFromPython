# 单元测试基础
# 什么是单元测试
# 单元测试是指一个自动化的测试
# 1.用来验证一小段代码（单元）的正确性
# 2.可以快速执行
# 3.在独立的环境中执行
# 常用的文件结构
# 新建tests文件夹与项目文件夹保持同级，并且tests文件夹中所有目录结构与项目文件夹保持一致
# 编写第一个单元测试
# Python提供了unittest模块:
# 1.测试类继承unittest.TestCase
# 2.测试类的名字以Test开头
# 3.测试方法的名字以test开头
# 运行单元测试
# 为了方便运行测试需要额外添加nose包和coverage包
# nose:可以运行所有的单元测试
# coverage:可以统计测试覆盖率
# 详细命令行参考day13_pip.py
# 官方文档：https://docs.python.org/zh-cn/3.13/library/unittest.html