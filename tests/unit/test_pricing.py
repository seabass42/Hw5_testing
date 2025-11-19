import pytest, math
from src.pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

@pytest.mark.parametrize("text, expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    ("$0.99",0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == expected

def test_format_currency():
    assert format_currency(12.2) == "$12.20"

def test_apply_discount():
    with pytest.raises(ValueError):
        apply_discount(100, -3)
    assert apply_discount(100, 10) == 90

def test_add_tax():
    with pytest.raises(ValueError):
        add_tax(40, -0.3)
    assert add_tax(30) == 32.1

def test_bulk_total():
    prices = [12.02, 43.05, 10.06, 14.07]
    assert bulk_total(prices, 3) == 82.20168
    