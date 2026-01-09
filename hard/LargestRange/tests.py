import pytest

from .solutions import largest_range, largest_range_space_optimized, largest_range_using_set, largest_range_numpy

test_data = [
    ([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6], [0, 7]),
    ([1], [1, 1]),
    ([1, 2], [1, 2]),
    ([4, 2, 1, 3], [1, 4]),
    ([4, 2, 1, 3, 6], [1, 4]),
    ([8, 4, 2, 10, 3, 6, 7, 9, 1], [6, 10]),
    ([19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14], [10, 19]),
    ([0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14], [-1, 19]),
    ([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2], [-7, 7]),
    ([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2], [-8, 19]),
    ([1, 1, 1, 3, 4], [3, 4]),
    ([-1, 0, 1], [-1, 1]),
    ([10, 0, 1], [0, 1]),
]


@pytest.mark.parametrize("array, expectedResult", test_data)
def test_largest_range(array, expectedResult):
    output = largest_range(array)
    assert output == expectedResult


@pytest.mark.parametrize("array, expectedResult", test_data)
def test_largest_range_space_optimized(array, expectedResult):
    output = largest_range_space_optimized(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_largest_range_using_set(array, expectedResult):
    output = largest_range_using_set(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_largest_range_numpy(array, expectedResult):
    output = largest_range_numpy(array)
    assert output == expectedResult