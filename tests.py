import pytest
from functions import add


def test_add_positive_numbers():
    """Test: Addition av positiva tal"""
    assert add(2, 3) == 5
    assert add(10, 15) == 25


def test_add_negative_numbers():
    """Test: Addition med negativa tal"""
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5
