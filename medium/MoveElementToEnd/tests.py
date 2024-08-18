import pytest

from medium.MoveElementToEnd.solution import moveElementToEnd

test_data = [
    ([2, 1, 2, 2, 2, 3, 4, 2], 2, 3, [1, 3, 4], [2, 2, 2, 2, 2]),
    ([], 3, 0, [], []),
    ([1, 2, 4, 5, 6], 3, 0, [], [1, 2, 4, 5, 6]),
    ([3, 3, 3, 3, 3], 3, 0, [], [3, 3, 3, 3, 3]),
    ([3, 1, 2, 4, 5], 3, 4, [1, 2, 4, 5], [3]),
    ([1, 2, 4, 5, 3], 3, 4, [1, 2, 4, 5], [3]),
    ([1, 2, 3, 4, 5], 3, 4, [1, 2, 4, 5], [3]),
    ([2, 4, 2, 5, 6, 2, 2], 2, 3, [4, 5, 6], [2, 2, 2, 2]),
    ([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5, 11, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], [5, 5, 5, 5, 5, 5]),
    ([1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5], 5, 11, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], [5, 5, 5, 5, 5, 5]),
    ([5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5, 11, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], [5, 5, 5, 5, 5, 5]),
]

@pytest.mark.parametrize("array, to_move, n, expectedStart, expectedEnd", test_data)
def test_isvalid_subsequence(array, to_move, n, expectedStart, expectedEnd):
    output = moveElementToEnd(array, to_move)
    outputStart = sorted(output[0:n])
    outputEnd = output[n:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd