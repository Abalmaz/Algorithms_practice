"""
  Given an array of integers between 1 and n, inclusive, where n is the length of the array,
  write a function that returns the first integer that appears more than once (when the array is
  read from left to right).
  In other words, out of all the integers that might occur more than once in the
  input array, your function should return the one whose first duplicate value
  has the minimum index.
  If no integer appears more than once, your function should return -1.
  Note that you're allowed to mutate the input array.
"""
from decorators.SpeedTestWrapper import timed

@timed(1)
def firstDuplicateValue(array: list[int]) -> int:
    """
    Pattern to use is a Hash Maps
    Time complexity: O(N),
    Space complexity: O(N)

    :param array: list[int]
    :return: int
    """
    if len(array) <= 1:
        return -1
    duplicate = {}
    for i in range(len(array)):
        if array[i] not in duplicate:
            duplicate[array[i]] = 1
        else:
            return array[i]
    return -1

@timed(1)
def firstDuplicateValue_v2(array: list[int]) -> int:
    """
    Pattern to use is the In-place Mutation technique
    Time complexity: O(N),
    Space complexity: O(1)

    :param array: list[int]
    :return: int
    """
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print(firstDuplicateValue(array))
print(firstDuplicateValue_v2(array))