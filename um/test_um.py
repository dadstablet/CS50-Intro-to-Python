from um import count
import pytest

def test_yumm():
    assert count("yumm") == "0"
    assert count("mum bum") == "0"
