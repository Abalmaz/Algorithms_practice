"""
Time complexity: O(nlog(n)  + mlog(m))
Space complexity: O(1)
"""
def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallest_sum = float('inf')
    smallest_pair = []
    index_one, index_two = 0, 0
    while index_one < len(arrayOne) and index_two < len(arrayTwo):
        current_sum = abs(arrayOne[index_one] - arrayTwo[index_two])
        if current_sum == 0:
            return [arrayOne[index_one], arrayTwo[index_two]]
        if smallest_sum > current_sum:
            smallest_sum = current_sum
            smallest_pair = [arrayOne[index_one], arrayTwo[index_two]]
        if arrayOne[index_one] < arrayTwo[index_two]:
            index_one += 1
        elif arrayTwo[index_two] < arrayOne[index_one]:
            index_two += 1
    return smallest_pair


# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallest_difference(arrayOne, arrayTwo))



