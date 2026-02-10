import pytest
from functions import add


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
