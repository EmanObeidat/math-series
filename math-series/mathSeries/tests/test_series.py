import pytest
from mathSeries.series import fibonacci
from mathSeries.series import lucas
from mathSeries.series import sum_series

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

def test_lucas():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_lucas():
    actual=lucas(7)
    expected=29
    assert actual==expected

def test_lucas():
    actual=lucas(8)
    expected=47
    assert actual==expected

def test_Sum():
    actual=sum_series(4, 0, 1)
    expected=3
    assert actual==expected