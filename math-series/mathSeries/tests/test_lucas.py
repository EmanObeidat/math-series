import pytest
from mathSeries.series import lucas

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