import pytest
from software.calc import Calc


def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9