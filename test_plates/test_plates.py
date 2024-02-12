from plates import is_valid

# def min_max_characters():
#     assert is_valid('CS') == False
#     assert is_valid('YABIEEE') == False

# def test_two_alphabets():
#     assert is_valid('CS50') == True

def test_leading_zero():
    assert is_valid('CS05') == False

def test_num_middle():
    assert is_valid('CS50P') == False

# def test_punctuation():
#     assert is_valid('CS50. [@_!$%^&*()<>?/\\|}{~:]#') == False
