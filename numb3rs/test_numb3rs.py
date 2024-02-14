from numb3rs import validate

def test_characters():
    assert validate('cat') == False
    assert validate('cat.cat.cat.cat') == False


def test_special_characters():
    assert validate('255,255,255,255') == False
    assert validate('255/255/255/255') == False
    assert validate('255;255;255;255') == False

def test_range_num():
    assert validate('512.512.512.512') == False
    assert validate('275.28.1.10') == False
    assert validate('28.278.1.10') == False
    assert validate('28.1.278.10') == False
    assert validate('28.1.10.278') == False

def test_length_address():
    assert validate('255.255.255.255.255') == False
