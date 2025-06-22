# 参数化测试用例
# 为什么需要参数化测试用例
# 针对同一个被测试函数需要进行多组数据的测试
# 使用patameterized插件实现
# pip install parametrized
# 使用装饰器@parametrize.expand([[1,true],[2,false]])来实现参数化测试
# 使用pytest实现
# 使用pytest.mark.parametrize
# 使用装饰器@pytest.mark.parametrize("num,expected_result",[[1,true],[2,false]])来实现参数化测试

# 关联mypj\basic\calculator.py和tests\basic\test_calculator.py还有test_odd.py