import pytest
from working import convert

def test_conversion():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"

def test_diff_format():
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("5:30 PM to 9 AM") == "17:30 to 09:00"

def test_invalid_format():
    with pytest.raises(ValueError) as error:
        convert('09:00 AM - 17:00 PM')
    assert error.type is ValueError

    with pytest.raises(ValueError) as error:
        convert('9 AM - 5 PM')
    assert error.type is ValueError

def test_out_of_range():
    with pytest.raises(ValueError) as error:
        convert('09:60 AM to 5 PM')
    assert error.type is ValueError

    with pytest.raises(ValueError) as error:
        convert('9 AM to 5:60 PM')
    assert error.type is ValueError
