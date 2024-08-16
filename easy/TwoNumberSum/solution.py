from decorators.SpeedTestWrapper import timed

"""
Time complexity: O(n*2)
Space complexity: O(1)
"""
@timed(10)
def two_number_sum(array, targetSum):
    for num in array:
        target = targetSum - num
        if target is not num and target in array:
            return [num, target]
    return []


"""
Time complexity: O(n)
Space complexity: O(n)
"""
@timed(10)
def two_number_sum2(array, targetSum):
    nums = {}
    for num in array:
        target = targetSum - num
        if target in nums:
            return [num, target]
        else:
            nums[num] = True
    return []

"""
Time complexity: nlog(n)
Space complexity: O(1)
"""
@timed(10)
def two_number_sum3(array, targetSum):
    array.sort()
    left_indx = 0
    right_indx = len(array) - 1
    while left_indx < right_indx:
        search_number = targetSum - array[left_indx]
        if search_number == array[right_indx]:
            return [array[left_indx], array[right_indx]]
        elif search_number < array[right_indx]:
            right_indx -= 1
        else:
            left_indx += 1
    return []

# array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
# targetSum = 163
# print(two_number_sum2(array, targetSum))

array = [3, 5, -4, 8, 11, 1, -1, 6]
big_array = [i for i in range(16, 100_00)] + array
targetSum = 10
print(two_number_sum(big_array, targetSum))
print(two_number_sum2(big_array, targetSum))
print(two_number_sum3(big_array, targetSum))