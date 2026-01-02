from decorators.SpeedTestWrapper import timed

"""
Time complexity: O(n)
Space complexity: O(1)
"""
# Solution 1
@timed(10)
def isMonotonic(array : list[int]) -> bool:
    if len(array) <= 2:
        return True
    is_incr = None
    for i in range(len(array) - 1):
        if is_incr is None:
            if array[i] < array[i+1]:
                is_incr = True
            elif array[i] > array[i+1]:
                is_incr = False
            else:
                continue
        else:
            if (array[i] < array[i+1]) == is_incr or (array[i] == array[i+1]):
                continue
            else:
                return False
    return True

# Solution 2
@timed(10)
def isMonotonic2(array : list[int]) -> bool:
    is_none_increasing = True
    is_none_decreasing = True
    for i in range(len(array) - 1):
        if array[i] < array[i+1]:
            is_none_decreasing = False
        elif array[i] > array[i+1]:
            is_none_increasing = False
    return is_none_increasing or is_none_decreasing





array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]
print(isMonotonic(array))
print(isMonotonic2(array))

# print(True and True) # True
# print(True and False) # False
# print(False and False) # False
#
# print(True or True) # True
# print(True or False) # True
# print(False or False) # False

