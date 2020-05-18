import pytest
import sys
from python.calc import Calc
sys.path.append("../data")

@pytest.fixture(scope="module")
def calc_setup():
    print("测试初始化start")
    calc = Calc()
    yield calc
    print("测试finish")

"""
方法定义在conftest.py中，就可以默认去执行
此例子是按照测试用例的方法名给各测试用例自动添加mark
然后通过pytest -m "add or div"这样的方式来执行名字中有add和div的用例
"""
def pytest_collection_modifyitems(session, items):
    print(type(items))
    for item in items:
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif 'minus' in item.nodeid:
            item.add_marker(pytest.mark.minus)
        elif 'multiply' in item.nodeid:
            item.add_marker(pytest.mark.multiply)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)

