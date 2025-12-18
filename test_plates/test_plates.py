from plates import is_valid

def test_True():
    assert is_valid("AAA222") == True

def test_short():
    assert is_valid("H") == False

def test_nums():
    assert is_valid("AAA022") == False
    assert is_valid("BB222A") == False
    assert is_valid("23AAA8") == False
    assert is_valid("123") == False

def test_other():
    assert is_valid("zzz.") == False
    assert is_valid("AA A2") == False
    assert is_valid("A AA.2") == False
