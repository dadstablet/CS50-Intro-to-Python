from project import get_composer_table, categorize_era, select_period
import pytest

def test_get_composer_table():
    assert get_composer_table() == False

def test_categorize_era():
    assert categorize_era("0.0.0.0.0") == False

def test_select_period():
    assert select_period("260.2.2.2") == False
    assert select_period("22.9.2.260") == False
