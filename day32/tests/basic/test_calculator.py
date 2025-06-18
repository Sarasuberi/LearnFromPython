import unittest
from mypj.basic.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):

        # Setup 准备部分
        cal = Calculator()
        expected_result = 10

        # Action 执行部分
        actual_result = cal.add(2, 3, 5)

        # Assert 断言部分
        self.assertEqual(expected_result,actual_result)
