"""
Time complexity: O(n)
Space complexity: O(1)
"""
from decorators.SpeedTestWrapper import timed

@timed(10)
def moveElementToEnd2(array, toMove):
    left_idx = 0
    right_idx = len(array) - 1
    while left_idx < right_idx:
        while left_idx < right_idx and array[right_idx] == toMove:
            right_idx -= 1
        if array[left_idx] == toMove:
            array[left_idx], array[right_idx] = array[right_idx], array[left_idx]
        left_idx += 1
    return array

"""
Time complexity: O(n)
Space complexity: O(1)
"""
@timed(10)
def moveElementToEnd(array, toMove):
    tmp = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[i], array[tmp] = array[tmp], array[i]
            tmp += 1
    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
bigArray = [i for i in range(3, 1_000_000)] + [array] + [i for i in range(3, 1_000_000)]

moveElementToEnd(bigArray, toMove)
moveElementToEnd2(bigArray, toMove)