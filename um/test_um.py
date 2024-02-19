from um import count

def test_only_word():
    assert count("um") == 1
    assert count(" um ") == 1

def test_word_between():
    assert count("thank um, a lot") == 1
    assert count("hello, um world") == 1

def test_case_sensitive():
    assert count("Um, you okay?") == 1

def test_with_um_word():
    assert count("this is your album!") == 0
