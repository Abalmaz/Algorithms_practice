import pytest

from easy.SortedSquaredArray.solution import sortedSquaredArray

test_data = [
    ([1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]),
    ([1], [1]),
    ([1, 2], [1, 4]),
    ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
    ([0], [0]),
    ([10], [100]),
    ([-1], [1]),
    ([-2, -1], [1, 4]),
    ([-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]),
    ([-10], [100]),
    ([-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]),
    ([-7, -3, 1, 9, 22, 30], [1, 9, 49, 81, 484, 900]),
    ([-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20], [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]),
    ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([-1, -1, 2, 3, 3, 3, 4], [1, 1, 4, 9, 9, 9, 16]),
    ([-3, -2, -1], [1, 4, 9]),
]

@pytest.mark.parametrize("array, expected", test_data)
def test_isvalid_subsequence(array, expected):
    actual = sortedSquaredArray(array)
    assert actual == expected
