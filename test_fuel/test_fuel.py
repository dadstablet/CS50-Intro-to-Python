from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    # assert convert("100/0") == "ZeroDivisionError"
    # assert convert("100/1") == "ValueError"
    # assert convert("1.1/1") == "ValueError"
    # assert convert("aaa/bbb") == "ValueError"
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
#     assert gauge("E") == "TypeError"
#     assert gauge(-199) == "ValueError"

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_value_error()
