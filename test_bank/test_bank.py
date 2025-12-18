from bank import value

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_h():
    assert value("hey buddy") == 20
    assert value("Hi") == 20

def test_other():
    assert value(123) == 100
    assert value("what") == 100
