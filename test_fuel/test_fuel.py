import pytest
from fuel import convert, gauge

def test_conversion():
    assert convert('1/4') == 25
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('4/4') == 100

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError) as error:
        convert('100/0')
    assert error.type is ZeroDivisionError

def test_value_error():
    with pytest.raises(ValueError) as error:
        convert('one/two')
    assert error.type is ValueError

def test_output():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(75) == '75%'
