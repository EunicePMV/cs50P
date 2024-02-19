import pytest
from seasons import get_mins
from datetime import date

TEST_DATE = "2000-01-01"

def test_valid_date():
    with pytest.raises(SystemExit) as error:
        get_mins("January 01, 1999", TEST_DATE)
    assert error.type is SystemExit
    assert str(error.value) == "Invalid date"

def test_word_mins():
    get_mins("1999-01-01", TEST_DATE) == "Five hundred twenty-five thousand, six hundred minutes"
