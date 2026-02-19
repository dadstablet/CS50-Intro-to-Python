from project import get_composer_table, categorize_era, select_period
import pytest

def test_get_composer_table():
    get_composer_table() = composers
    assert len(get_composer_table() ) == 669
    assert composers['name'].dtype == str

def test_categorize_era():
    assert categorize_era(1600) == 'Baroque'
    assert cateogorize_era(1735) == 'Baroque'
    assert categorize_era(1815) == 'Classical'

def test_select_period():
    assert select_period('Bach') == 'Baroque'
    assert select_period('Romantic') == 'Romantic'
    assert select_period('hello world') == ValueError
    assert select_period('clAssIcal') == 'Classical'
