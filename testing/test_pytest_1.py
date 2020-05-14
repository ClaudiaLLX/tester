
from python.calc import Calc
import math

class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        num = self.calc.add(1, 2)
        print(num)
        assert 3 == num

    def test_add_2(self):
        num = self.calc.add(-1, -2)
        print(num)
        assert -3 == num

    def test_add_3(self):
        num = self.calc.add(2.8, 4.2)
        print(num)
        assert 7.0 == num

    def test_div_1(self):
        num = self.calc.div(2, 2)
        print(num)
        assert math.isclose(1.0, num)

    def test_div_2(self):
        num = self.calc.div(-2, -4)
        print(num)
        assert math.isclose(0.5, num)

    def test_div_3(self):
        num = self.calc.div(3.6, 1.5)
        print(num)
        assert math.isclose(2.4, num)

    def test_minus_1(self):
        num = self.calc.minus(1,5)
        print(num)
        assert math.isclose(-4, num)

    def test_minus_2(self):
        num = self.calc.minus(10,5)
        print(num)
        assert math.isclose(5, num)

    def test_minus_3(self):
        num = self.calc.minus(3.3,2.2)
        print(num)
        assert math.isclose(1.1, num)

    def test_multiply_1(self):
        num = self.calc.multiply(1,5)
        print(num)
        assert 5 == num

    def test_multiply_2(self):
        num = self.calc.multiply(-1,5)
        print(num)
        assert -5 == num

    def test_multiply_3(self):
        num = self.calc.multiply(1.5,4.5)
        print(num)
        assert 6.75 == num