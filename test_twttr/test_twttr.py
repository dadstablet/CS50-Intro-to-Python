from twttr import shorten

def test_heLLO():
    x = 'heLLO'
    assert shorten(x) == "hLL"

# def test_HELLO():
#     x = 'HELLO'
#     assert shorten(x) == 'HLL'

def test_int():
    x = 1
    assert shorten(x) == "Error"
