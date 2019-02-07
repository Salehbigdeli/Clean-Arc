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