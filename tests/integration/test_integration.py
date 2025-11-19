import pytest
from src.order_io import load_order, write_receipt
from src.pricing import bulk_total

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    items = load_order(input_file)
    prices = [price for (_name, price) in items]
    total = bulk_total(prices, 10, 0.1)
    write_receipt(tmp_path / "receipt.txt", items, discount_percent=10, tax_rate=0.1)

    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL:" in output_text