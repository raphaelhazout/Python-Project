from unittest import TestCase, mock
from Package1.Calculator import *

class TestCalculator(TestCase):
    @mock.patch('Package1.Calculator.Calculator.sum_numbers', return_value = 10)
    def test_sum_numbers(self, mock_sum_numbers):
        calc = Calculator(4,6)
        res = calc.sum_numbers()
        print(res)
        self.assertTrue(res == 10)
