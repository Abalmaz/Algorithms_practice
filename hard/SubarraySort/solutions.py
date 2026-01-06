"""
  Write a function that takes in an array of at least two integers and that
  returns an array of the starting and ending indices of the smallest subarray
  in the input array that needs to be sorted in place in order for the entire
  input array to be sorted (in ascending order).
  If the input array is already sorted, the function should return [-1, -1]
"""
from decorators.SpeedTestWrapper import timed


@timed(10)
def subarraySort_v1(array):
    leftValue = -1
    rightValue = -1
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < maxValue:
            leftValue = i
        else:
            maxValue = array[i]
    minValue = array[len(array) - 1]
    for i in reversed(range(0, len(array))):
        if array[i]> minValue:
            rightValue = i
        else:
            minValue = array[i]
    return [rightValue, leftValue]

@timed(10)
def subarraySort_v2(array):
    min_out_of_range = float("inf")
    max_out_of_range = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_range = min(min_out_of_range, num)
            max_out_of_range = max(max_out_of_range, num)
    if min_out_of_range == float("inf"):
        return [-1, -1]
    subarray_left_idx = 0
    while min_out_of_range >= array[subarray_left_idx]:
        subarray_left_idx += 1
    subarray_right_idx = len(array) - 1
    while max_out_of_range <= array[subarray_right_idx]:
        subarray_right_idx -= 1
    return [subarray_left_idx, subarray_right_idx]

def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array) - 1:
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]


array = [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19]
print(subarraySort_v1(array))
print(subarraySort_v2(array))
