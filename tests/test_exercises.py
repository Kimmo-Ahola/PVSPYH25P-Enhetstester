import math
import pytest
from functions import (
    add,
    capitalize_words,
    count_vowels,
    divide,
    multiply,
    reverse_string,
)


def test_add_positive_numbers():
    """
    Test: Addition av positiva tal
    The test fails because the function is not yet implemented.
    """
    assert add(2, 3) == 5
    assert add(10, 15) == 25


def test_add_negative_numbers():
    """
    Test: Addition med negativa tal
    The test fails because the function is not yet implemented.
    """
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5


def test_multiply_positive():
    # TODO: Skriv ditt test här
    first = 3
    second = 3

    result = multiply(first, second)

    assert result == 3 * 3


def test_multiply_with_zero():

    assert multiply(1, 0) == 0
    assert multiply(0, 1) == 0
    assert multiply(0, 0) == 0


def test_multiply_negative():

    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(2, -2) == -4


def test_division_by_zero():
    assert divide(1, 0) == math.inf


def test_division_positive():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(10, -2) == -5


def test_capitalize_single_word():
    assert capitalize_words("kimmo") == "Kimmo"
    assert capitalize_words("KIMMO") == "Kimmo"


def test_capitalize_multiple_words():
    assert capitalize_words("kimmo ahola") == "Kimmo Ahola"
    assert capitalize_words("kimmo kristiAN ahola") == "Kimmo Kristian Ahola"


def test_capitalize_already_capitalized():
    assert capitalize_words("Kimmo Kristian Ahola") == "Kimmo Kristian Ahola"
    assert capitalize_words("1 1 1") == "1 1 1"


def test_reverse():
    assert reverse_string("Hej") == "jeH"
    assert reverse_string("") == ""
    assert reverse_string("111!") == "!111"


def test_count_en_vowels():
    assert count_vowels("Hello") == 2
    assert count_vowels("Gym") == 0
    assert count_vowels("Hallå") == 1


def test_count_swe_vowels():
    assert count_vowels("Hallå", "sv") == 2
    assert count_vowels("Gym", "sv") == 1


# Exempel på parametriserat test
# a, b och expected är det som skickas in i testfunktionen nedan.
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add_parametrized(a, b, expected):  # Här är a, b och expected
    """Test: Addition med flera testfall"""
    # a och b skickas in i add. expected är vårt förväntade resultat
    # vi har här en enda rad istället för att skriva flera rader med assert
    assert add(a, b) == expected
