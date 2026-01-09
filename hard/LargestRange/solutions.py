"""
  Write a function that takes in an array of integers and returns an array of
  length 2 representing the largest range of integers contained in that array.
  The first number in the output array should be the first number in the range,
  while the second number should be the last number in the range.
  A range of numbers is defined as a set of numbers that come right after each
  other in the set of real integers. For instance, the output array [2, 6]
  represents the range {2, 3, 4, 5, 6}, which
  is a range of length 5. Note that numbers don't need to be sorted or adjacent
  in the input array in order to form a range.
  You can assume that there will only be one largest range.
"""
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

from decorators.SpeedTestWrapper import timed


# @timed(10)
def largest_range(array: list[int]) -> list[int]:
    """
    Pattern to use is Hash Maps or Knowing What to Track
    Time complexity: O(N),
    Space complexity: O(N)

    :param array: list[int]
    :return: array[int]
    """
    numbers = {x: True for x in array}
    best_range = []
    longest_length = 0
    for num in array:
        if num not in numbers:
            continue
        numbers[num] = False
        current_length = 1
        left = num - 1
        right = num + 1
        # Expand left
        while left in numbers:
            numbers[left] = False
            current_length += 1
            left -= 1
        # Expand right
        while right in numbers:
            numbers[right] = False
            current_length += 1
            right += 1

        if current_length > longest_length:
            longest_length = current_length
            best_range = [left + 1, right - 1]
    return best_range

# @timed(10)
def largest_range_space_optimized(array: list[int]) -> list[int]:
    """
    Sort input array in-place, if memory is extremely limited.
    Time complexity: O(N * logN),
    Space complexity: O(1)

    :param array: list[int]
    :return: list[int]
    """
    if not array:
        return []
    array.sort()
    best_range = [array[0], array[0]]
    longest_length = 0
    current_start = array[0]
    current_length = 1

    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            continue
        if array[i] == array[i - 1] + 1:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                best_range = [current_start, array[i - 1]]
            current_start = array[i]
            current_length = 1
    if current_length > longest_length:
        best_range = [current_start, array[-1]]

    return best_range


# @timed(10)
def largest_range_using_set(array: list[int]) -> list[int]:
    """
    Using set prevents the algorithm from re-visiting numbers multiple times.
    By checking for num - 1, we ensure that the while loop only runs for the absolute start of a consecutive sequence.
    Time complexity: O(N),
    Space complexity: O(N)

    :param array: list[int]
    :return: list[int]
    """
    nums = set(array)
    best_range = []
    longest_length = 0
    for num in nums:
        if num - 1 not in nums:
            i = num
            while i in nums:
                i += 1
            current_length = i - num
            if current_length > longest_length:
                longest_length = current_length
                best_range = [num, i - 1]
    return best_range

def largest_range_numpy(arr: list[int]) -> list[int]:
    """
    The NumPy solution follows the Sort and Search pattern.
    Time complexity: O(N * logN),
    Space complexity: O(N)

    :param arr: list[int]
    :return: list[int]
    """
    if len(arr) == 0:
        return []
    sorted_unique = np.unique(arr)
    diffs = np.diff(sorted_unique)
    breaks = np.concatenate(([True], diffs != 1, [True]))
    break_indices = np.where(breaks)[0]
    lengths = np.diff(break_indices)
    max_idx = np.argmax(lengths)
    start_val = sorted_unique[break_indices[max_idx]]
    end_val = sorted_unique[break_indices[max_idx + 1] - 1]

    return [int(start_val), int(end_val)]

# array = [-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]
# print(largestRange(array))
# print(largestRange_space_optimized(array))
# print(largestRange_using_set(array))

sizes = [100_000, 5_000_000]
set_times, sort_times, numpy_times = [], [], []

for size in sizes:
    # Generate random data with potential ranges
    test_data = [random.randint(0, size * 2) for _ in range(size)]

    # Run each test multiple times to average out noise
    t_numpy = timeit.timeit(lambda: largest_range_numpy(test_data), number=10)
    t_set = timeit.timeit(lambda: largest_range_using_set(test_data), number=10)
    t_sort = timeit.timeit(lambda: largest_range_space_optimized(test_data), number=10)

    numpy_times.append(t_numpy / 5)
    set_times.append(t_set / 5)
    sort_times.append(t_sort / 5)

# Plotting Results
plt.plot(sizes, set_times, label='O(N) Set Solution', marker='x')
plt.plot(sizes, sort_times, label='O(N log N) Sort Solution', marker='s')
plt.plot(sizes, numpy_times, label='O(N log N) Numpy Version', marker='o')
plt.xlabel('Input Size (N)')
plt.ylabel('Average Execution Time (Seconds)')
plt.title('Algorithm Performance Comparison: Largest Range')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()