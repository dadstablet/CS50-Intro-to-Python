from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("100/1")
        convert("1.1/1")
        convert("aa/nb")
        convert("-1/2")
        convert("1/-2")
        convert("-1/-2")
        gauge(-1)
        gauge(-.2)
