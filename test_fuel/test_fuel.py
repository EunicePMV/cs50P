import pytest
from fuel import convert, gauge

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError) as error:
        convert('100/0')
    assert error.type is ZeroDivisionError

def test_value_error():
    with pytest.raises(ValueError) as error:
        convert('one/two')
    assert error.type is ValueError

def test_output():
    
