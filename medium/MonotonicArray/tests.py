import pytest

from .solutions import isMonotonic

test_data = [
    ([-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True),
    ([], True),
    ([1], True),
    ([1, 2], True),
    ([2, 1], True),
    ([1, 5, 10, 1100, 1101, 1102, 9001], True),
    ([-1, -5, -10, -1100, -1101, -1102, -9001], True),
    ([-1, -5, -10, -1100, -900, -1101, -1102, -9001], False),
    ([1, 2, 0], False),
    ([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], False),
    ([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11], True),
    ([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11], False),
    ([-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11], True),
    ([-1, -1, -1, -1, -1, -1, -1, -1], True),
    ([1, 2, -1, -2, -5], False),
    ([-1, -5, 10], False),
    ([2, 2, 2, 1, 4, 5], False),
    ([1, 1, 1, 2, 3, 4, 1], False),
    ([1, 2, 3, 3, 2, 1], False),
]

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_isvalid_subsequence(array, expectedResult):
    output = isMonotonic(array)
    assert output == expectedResult
