import pytest

from .solutions import minRewards

test_data = [
    ([8, 4, 2, 1, 3, 6, 7, 9, 5], 25),
    ([1], 1),
    ([5, 10], 3),
    ([10, 5], 3),
    ([4, 2, 1, 3], 8),
    ([0, 4, 2, 1, 3], 9),
    ([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0], 52),
    ([2, 1, 4, 3, 6, 5, 8, 7, 10, 9], 15),
    ([800, 400, 20, 10, 30, 61, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53], 93),
]


@pytest.mark.parametrize("array, expectedResult", test_data)
def test_min_rewards(array, expectedResult):
    output = minRewards(array)
    assert output == expectedResult
