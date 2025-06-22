# 测试覆盖率
# 测试覆盖率是衡量代码被测试覆盖程度的指标，通常用百分比表示。测试覆盖率越高，说明测试覆盖的代码范围越广，测试的可靠性越高。
# 测试覆盖率统计的是被测试代码在单元测试的过程中有多少行代码被执行到了
# 覆盖率 = 执行到的代码行数/代码总行数
# 一般是达到80%以上，才能说明测试覆盖的代码比较全面
# Python中常用的测试覆盖率工具是coverage，它可以帮助我们统计代码的测试覆盖率，并提供详细的报告。
# 安装coverage：pip install coverage
# 统计测试覆盖率
# python -m coverage run -m unittest discover
# 查看覆盖率报告
# python -m coverage report 
# 生成HTML格式的覆盖率报告
# python -m coverage html