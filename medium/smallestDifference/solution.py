def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    diff_sums = {}
    for i in range(len(arrayOne)):
        j = 0
        while j < len(arrayTwo) - 1:
            diff_sum_first_pair = abs(arrayOne[i] - arrayTwo[j])
            if diff_sum_first_pair == 0:
                diff_sums[diff_sum_first_pair] = [i, j]
                break
            diff_sum_second_pair = abs(arrayOne[i] - arrayTwo[j + 1])
            if diff_sum_second_pair == 0:
                diff_sums[diff_sum_second_pair] = [i, j + 1]
                break
            if diff_sum_second_pair > diff_sum_first_pair:
                diff_sums[diff_sum_first_pair] = [i, j]
                break
            if diff_sum_second_pair < diff_sum_first_pair and j == len(arrayTwo) - 2:
                diff_sums[diff_sum_second_pair] = [i, j + 1]
                break
            j += 1
    first, second = diff_sums.get(min(diff_sums))
    return [arrayOne[first], arrayTwo[second]]


# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
arrayOne = [240, 124, 86, 111, 2, 84, 954, 27, 89]
arrayTwo = [1, 3, 954, 19, 8]
print(smallest_difference(arrayOne, arrayTwo))