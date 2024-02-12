from twttr import shorten

def test_lower_vowels():
    assert shorten('love') == 'lv'
    assert shorten('yabiu') == 'yb'

def test_upper_vowels():
    assert shorten('LOVE') == 'LV'
    assert shorten('YABIU') == 'YB'

def test_number():
    assert shorten('love123') == 'lv'
    assert shorten('yabiu08') == 'yb'

def test_punctuation():
    assert shorten('l,o,v,e') == 'lv'
    assert shorten('yabiu~!@#$%^&*(),./;"[]|') == 'yb'

# def main():
#     test_twttr()

# def test_twttr():
#     vowel = 'aeiouAEIOU'
#     if shorten('love') != 'lv':
#         print('love should be lv')
#     if shorten('yabiu') != 'yb':
#         print('yab should be yb')
#     if shorten('LOVE') != 'LV':
#         print('LOVE should be LV')
#     if shorten('YABIU') != 'YB':
#         print('YABIU should be YB')

# if __name__ == "__main__":
#     main()
