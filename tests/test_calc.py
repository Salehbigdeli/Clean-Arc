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

def test_subtract_two_numbers():
    c = Calc()
    res = c.sub(6, 2)
    assert res == 4