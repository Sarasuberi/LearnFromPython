# PyTest框架
# 什么是PyTest
# PyTest是一个机遇Python语言的第三方的测试框架，可以用来编写和运行测试用例，支持单元测试和功能测试，支持测试用例的自动发现和执行，支持测试用例的分组和标记，支持测试报告的生成。
# PyTest的优点
# 1.语法简单
# 2.自动检测测试代码
# 3.跳过指定测试
# 4.开源
# PyTest的测试环境
# 1.安装PyTest：pip install pytest
# 2.运行PyTest：pytest/pytest test_xxx.py
# 自动查找test_*.py和*_test.py文件中的测试用例
# 自动查找测试文件中的test_开头的函数和Test开头的类中的test_开头的方法
# PyTest的常用参数
# -v：显示详细信息,输出详细的执行信息，比如文件及用例名称等
# -s：显示标准输出，输出调试信息，比如print的打印信息
# -k：指定测试用例
# -x：遇到错误时停止
# pytest --lf  # 仅运行上次失败的测试
# 跳过测试
# 跳过测试的方式有两种
# 1.使用@pytest.mark.skip装饰器
# 2.使用@pytest.mark.skipif装饰器