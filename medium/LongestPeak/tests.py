import pytest

from .solutions import longestPeak, longestPeak_v2, longestPeak_Refined

test_data = [
    ([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], 6),
    ([], 0),
    ([1, 3, 2], 3),
    ([1, 2, 3, 4, 5, 1], 6),
    ([5, 4, 3, 2, 1, 2, 1], 3),
    ([5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10], 5),
    ([5, 4, 3, 2, 1, 2, 10, 12], 0),
    ([1, 2, 3, 4, 5, 6, 10, 100, 1000], 0),
    ([1, 2, 3, 3, 2, 1], 0),
    ([1, 1, 3, 2, 1], 4),
    ([1, 2, 3, 2, 1, 1], 5),
    ([1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1], 9),
    ([1, 2, 3, 3, 4, 0, 10], 3),
]

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_spiral_traverse_v1(array, expectedResult):
    output = longestPeak(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_spiral_traverse_v2(array, expectedResult):
    output = longestPeak_v2(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_spiral_traverse_v3(array, expectedResult):
    output = longestPeak_Refined(array)
    assert output == expectedResult