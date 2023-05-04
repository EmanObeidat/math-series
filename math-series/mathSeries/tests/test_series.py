import pytest
from mathSeries.series import fibonacci


def test_fab1():
    actual=fibonacci(1)
    expected=1
    assert actual==expected

def test_fab2():
    actual=fibonacci(2)
    expected=1
    assert actual==expected

def test_fab3():
    actual=fibonacci(3)
    expected=2
    assert actual==expected