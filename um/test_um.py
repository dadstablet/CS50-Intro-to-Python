from um import count
import pytest

def test_yumm():
    assert count("um") == 0
    assert count("mum bum") == 0

def test_case():
    assert count("Um, UM!") == 2
    assert count("UM, hi") == 1
