from numb3rs import validate
import pytest

def test_lead0():
    assert validate("001.22.22.22") == "False"
    # assert validate("0.00.00.0") == "False"

def test_chars():
    assert validate("dog.cat") == "False"
    assert validate("2.2.2.cow") == "False"

def test_greaterthan255():
    assert validate("260.2.2.2") == "False"
    assert validate("22.9.2.260") == "False"
