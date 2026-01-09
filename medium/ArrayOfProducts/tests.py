import pytest

from .solutions import arrayOfProducts, arrayOfProducts_v2

test_data = [
    ([5, 1, 4, 2], [8, 40, 10, 20]),
    ([1, 8, 6, 2, 4], [384, 48, 64, 192, 96]),
    ([-5, 2, -4, 14, -6], [672, -1680, 840, -240, 560]),
    ([9, 3, 2, 1, 9, 5, 3, 2], [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]),
    ([4, 4], [4, 4]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([-1, -1, -1], [1, 1, 1]),
    ([-1, -1, -1, -1], [-1, -1, -1, -1]),
    ([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
]


@pytest.mark.parametrize("array, expectedResult", test_data)
def test_array_of_products(array, expectedResult):
    output = arrayOfProducts(array)
    assert output == expectedResult

@pytest.mark.parametrize("array, expectedResult", test_data)
def test_array_of_products_v2(array, expectedResult):
    output = arrayOfProducts_v2(array)
    assert output == expectedResult
