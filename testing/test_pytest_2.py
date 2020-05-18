import pytest
import yaml
from python.calc import Calc
import math
import sys
sys.path.append("../data")

def load_step():
    with open("../data/steps.yaml",'r') as f:
        f.seek(0)
        steps=yaml.safe_load(f)
        return steps


class TestCalc2:

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("../data/calc_test.yaml"))["add"])
    def calc_add_test(self, calc_setup, a, b, expected):
        steps_load = load_step()
        for step in steps_load:
            if 'add' == step:
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    num = calc_setup.add(a, b)
                    print(num)
                    assert expected == num
                else:
                    pytest.raises(BaseException)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("../data/calc_test.yaml"))["div"])
    def calc_div_test(self, calc_setup, a, b, expected):
        steps_load = load_step()
        for step in steps_load:
            if 'div' == step:
                if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
                    num = calc_setup.div(a, b)
                    print(num)
                    assert math.isclose(expected, round(num,2))
                else:
                    pytest.raises(BaseException)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("../data/calc_test.yaml"))["minus"])
    def calc_minus_test(self, calc_setup, a, b, expected):
        steps_load = load_step()
        for step in steps_load:
            if 'minus' == step:
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    num = calc_setup.minus(a, b)
                    print(num)
                    assert num == expected
                else:
                    pytest.raises(BaseException)

    @pytest.mark.parametrize("a, b, expected", yaml.safe_load(open("../data/calc_test.yaml"))["multiply"])
    def calc_multiply_test(self, calc_setup, a, b, expected):
        steps_load = load_step()
        for step in steps_load:
            if 'multiply' == step:
                if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                    num = calc_setup.multiply(a, b)
                    print(num)
                    assert round(num,4) == expected
                else:
                    pytest.raises(BaseException)