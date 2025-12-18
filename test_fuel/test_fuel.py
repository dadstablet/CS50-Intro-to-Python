from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("100/0") == "ZeroDivisionError"

