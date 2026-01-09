"""
  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array. In other words, the value at output[i]
  is equal to the product of every number in the input array other than input[i].
  Note that you're expected to solve this problem without using division.
"""
from decorators.SpeedTestWrapper import timed


@timed(10)
def arrayOfProducts(array):
    """
      Solution using Knowing What to Track pattern, specifically utilizing Prefix and Suffix Products.

      Time complexity: O(N),
      Space complexity: O(N)
    """
    length = len(array)
    output = [1] * length

    left_product = 1
    for i in range(length):
        output[i] = left_product
        left_product *= array[i]
    right_product = 1
    for i in range(length - 1, -1, -1):
        output[i] *= right_product
        right_product *= array[i]
    return output


@timed(10)
def arrayOfProducts_v2(array):
    """
      Solution using division.

      Time complexity: O(N),
      Space complexity: O(N)
    """
    total_multiply = 1
    for num in array:
        total_multiply *= num
    if total_multiply == 0:
        return [0] * len(array)
    return [total_multiply // num for num in array]


array = [5, 1, 4, 2]
print(arrayOfProducts(array))
print(arrayOfProducts_v2(array))