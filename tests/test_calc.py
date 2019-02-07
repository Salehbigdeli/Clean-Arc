import pytest
from software.calc import Calc


def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9

def test_adding_multiple_numbers():
    c = Calc()
    res = c.add(1, 2, 3)
    assert res == 6

def test_add_many_nums():
    c = Calc()
    res = c.add(*range(100))
    assert res == 4950
    res = c.add()
    assert res == 0

def test_subtract_two_numbers():
    c = Calc()
    res = c.sub(6, 2)
    assert res == 4
    res = c.sub(32, 16)
    assert res == 16

def test_multiply_two_numbers():
    c = Calc()
    res = c.mul(3, 7)
    assert res == 21

def test_multiply_many_numbers():
    c = Calc()
    res = c.mul(4, 5, 2)
    assert res == 40
    with pytest.raises(Exception):
        res = c.mul()

def test_divide_two_numbers():
    c = Calc()
    res = c.div(3, 4)
    assert res == .75
