from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("100/0") == "ZeroDivisionError"
    assert convert("100/1") == "ValueError"
    assert convert("1.1/1") == "ValueError"
    assert convert("aaa/bbb") == "ValueError"
    assert convert("1/2") == 50

# def test_gauge():

