from audioop import reverse

from decorators.SpeedTestWrapper import timed


"""
Time complexity: O(n)
Space complexity: O(n)
"""
@timed(1)
def sortedSquaredArray(array):
    left_point = 0
    right_point = len(array) - 1
    indx = right_point
    result = [0] * len(array)
    while indx >= 0:
        left_sqr = abs(array[left_point])
        right_sqr = abs(array[right_point])
        if left_sqr < right_sqr:
            result[indx] = right_sqr ** 2
            right_point -= 1
        else:
            result[indx] = left_sqr **2
            left_point += 1
        indx -= 1
    return result


@timed(1)
def sortedSquaredArray2(array):
    sorted_squared_array = [0 for _ in range(len(array))]
    smaller_idx = 0
    larger_idx = len(array) - 1
    for idx in reversed(range(len(array))):
        smaller_value = array[smaller_idx]
        larger_value = array[larger_idx]
        if abs(smaller_value) > abs(larger_value):
            sorted_squared_array[idx] = smaller_value ** 2
            smaller_idx += 1
        else:
            sorted_squared_array[idx] = larger_value ** 2
            larger_idx -= 1
    return sorted_squared_array


array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
big_array = [i for i in range(-100_000, 100_000)]
sortedSquaredArray(big_array)
sortedSquaredArray2(big_array)

