from numb3rs import validate
import pytest

def test_first_byte():
    assert validate("8") == False

def test_five_byte():
    assert validate("0.0.0.0.0") == False

def test_greaterthan255():
    assert validate("260.2.2.2") == False
    assert validate("22.9.2.260") == False
