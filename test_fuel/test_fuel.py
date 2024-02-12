import pytest
from fuel import convert, gauge

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        1/0

def test_value_error():
    with pytest.raises(ValueError):
        'one'/1
