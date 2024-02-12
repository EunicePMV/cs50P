from twttr import shorten

def test_lower_vowels():
    assert shorten('love') == 'lv'
    assert shorten('yabiu') == 'yb'

def test_upper_vowels():
    assert shorten('LOVE') == 'LV'
    assert shorten('YABIU') == 'YB'

def test_number():
    assert shorten('love123') == 'lv123'
    assert shorten('yabiu08') == 'yb08'

def test_punctuation():
    assert shorten('l,o,v,e') == 'l,,v,'
    assert shorten('yabiu~!@#$%^&*(),./;"[]|') == 'yb~!@#$%^&*(),./;"[]|'
