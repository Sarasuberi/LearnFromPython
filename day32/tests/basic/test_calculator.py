import unittest
from parameterized import parameterized
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

    @parameterized.expand([1, True], [2, False])
    def test_is_odd(self, num: int, expected_result: bool):

        # Setup 准备部分
        cal = Calculator()

        # Action 执行部分
        actual_result = cal.is_odd(num)

        # Assert 断言部分
        assert expected_result == actual_result
