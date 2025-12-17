from twttr import shorten

def test_hello():
    x = 'hello'
    assert shorten(x) == "hll"

def test_HELLO():
    x = 'HELLO'
    assert shorten(x) == 'HLL'

# def test_int():
#     x = 1
#     assert shorten(x) == 1
