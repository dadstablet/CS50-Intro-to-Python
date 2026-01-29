from working import convert
import pytest

def test():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:70 PM")

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
