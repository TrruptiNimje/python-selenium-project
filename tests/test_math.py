import pytest


def add_two_numbers(a, b):
    return a + b


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(4, 5) == 9, "The sum of 4 and 5 should be 9 "


@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400 "
