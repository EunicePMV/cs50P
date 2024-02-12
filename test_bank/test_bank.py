from bank import value

def test_hello():
    assert value('hello') == 0

def test_h():
    assert value('hi') == 20

def test_other_greetings():
    assert value('good morning') == 100

def test_capitalization():
    assert value('HELLO') == 0
    assert value('HI') == 20
    assert value('GOOD MORNING') == 100
