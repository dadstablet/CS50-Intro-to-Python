from project import get_composer_table, categorize_era, select_period
import pytest

def test_get_composer_table():
    assert len(get_composer_table()) == 669

def test_categorize_era():
    assert categorize_era(1600) == 'Baroque'
    assert categorize_era(1735) == 'Baroque'
    assert categorize_era(1815) == 'Classical'

def test_select_period():
    with pytest.raises(ValueError):
        select_period('hello world')
    assert select_period('Bach') == 'Baroque'
    assert select_period('Romantic') == 'Romantic'
    assert select_period('clAssIcal') == 'Classical'
