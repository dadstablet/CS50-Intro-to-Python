from twttr import shorten
import random

def test_heLLO():
    x = 'heLLO'
    assert shorten(x) == "hLL"

# def test_HELLO():
#     x = 'HELLO'
#     assert shorten(x) == 'HLL'

def test_int():
    x = random.randint()
    assert shorten(x) == x
