import pytest
from app.calculator import calculate


def test_valid_calculations():
    assert calculate("1 + 1") == 2
    assert calculate("2 * 3") == 6
    assert calculate("10 / 2") == 5.0
    assert calculate("5 - 3") == 2


def test_division_by_zero():
    assert calculate("1 / 0") == "Division by zero"


def test_invalid_input():
    assert calculate("1 +") == "Invalid Input"


def test_unhandled_error():
    assert calculate("abc") == "unhandled error occurred"
    assert calculate(None) == "unhandled error occurred"
