import pytest
from calculator_dir import calculator
from calculator_dir.calculator import add as scitej
from calculator_dir.calculator import subtract
from calculator_dir.calculator import multiply
from calculator_dir.calculator import divide


def test_scitej():
    assert scitej(1, 4) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(3, 5) == 15

def test_divide():
    assert divide(6, 2) == 3
