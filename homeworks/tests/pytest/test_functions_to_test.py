from functions_to_test import Calculator
import pytest


def test_add():
    assert Calculator.add(100, 5) == 105


def test_substract():
    assert Calculator.subtract(3, 5) == -2


def test_multiply():
    assert Calculator.multiply(29, 12) == 348


def test_divide():
    assert Calculator.divide(120, 60) == 2
    with pytest.raises(ValueError):
        Calculator.divide(4, 0)
