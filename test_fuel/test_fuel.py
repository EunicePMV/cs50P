import pytest
from fuel import convert, gauge

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError) as error:
        convert('100/0')
    assert error.type is ZeroDivisionError
