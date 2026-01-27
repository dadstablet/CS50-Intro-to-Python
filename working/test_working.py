from working import convert
import pytest

def test_am():
    assert convert("5 AM") == ValueError
