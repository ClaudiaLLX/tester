import unittest

from python.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add1(self):
        self.calc = Calc()
        num = self.calc.add(1,2)
        self.assertEqual(3, num)