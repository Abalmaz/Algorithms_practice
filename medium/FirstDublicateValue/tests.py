import pytest

from .solutions import firstDuplicateValue, firstDuplicateValue_v2

test_data = [
    ( [2, 1, 5, 2, 3, 3, 4], 2

    ),
    (
        [2, 1, 5, 3, 3, 2, 4], 3

    ),
    (
        [1, 1, 2, 3, 3, 2, 2], 1

    ),
    (
        [], -1
    ),
    (
        [1], -1

    ),
    (
        [1, 1], 1

    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10], 10

    ),
    (
        [2, 1, 1], 1

    ),
    (
        [2, 2, 2, 2, 2, 2, 2, 2, 2], 2

    ),
(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1

),
]


@pytest.mark.parametrize("array, expectedResult", test_data)
def test_first_dublicate_value(array, expectedResult):
    output = firstDuplicateValue(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_first_dublicate_value_v2(array, expectedResult):
    output = firstDuplicateValue_v2(array)
    assert output == expectedResult