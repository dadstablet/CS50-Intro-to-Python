from numb3rs import validate
import pytest

def test_lead0():
    assert validate("001.22.22.22") == "Invalid"
    assert validate("0.00.00.0") == "Valid"

# def test_chars():
#     with pytest.raises(AttributeError):
#         validate("dog.cat")
#         validate("2.2.2.cow")

# def test_greaterthan255():
#     assert validate("260.2.2.2") == "Invalid"
#     assert validate("22.9.2.260") == "Invalid"
