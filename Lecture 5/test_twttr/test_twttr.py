from twttr import shorten
import random

def test_heLLO():
    x = 'heLLO.'
    assert shorten(x) == "hLL."

def test_HELLO():
    x = 'HELLO1'
    assert shorten(x) == "HLL1"

# def test_int():
#     x = random.randint(-999,999)
#     assert shorten(x) == x

# def test_punct():
#     x = "H..."
#     assert shorten(x) == "H..."
