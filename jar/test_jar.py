import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError) as error:
        jar = Jar(-1)
    assert error.type is ValueError

    with pytest.raises(ValueError) as error:
        jar = Jar("cookies")
    assert error.type is ValueError


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(2)
    assert jar.size == 3


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(2)
    assert jar.size == 8
