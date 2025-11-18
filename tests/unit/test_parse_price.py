import pytest
from src.pricing import parse_price

@pytest.mark.parametrize("text, expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    ("$0.99",0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == expected