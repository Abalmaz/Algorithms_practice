from decorators.SpeedTestWrapper import timed

"""
Time complexity: avg = O(n**2), worst case = O(n**3)
Space complexity: O(n**2)
"""

@timed(1)
def fourNumberSum(array, targetSum):
    twoNumberSum  = {}
    result = []
    for i in range(0, len(array)-1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if currentSum in twoNumberSum:
                twoNumberSum[currentSum].append([i, j])
            else:
                twoNumberSum[currentSum] = [[i, j]]
            if difference in twoNumberSum:
                for pair in twoNumberSum[difference]:
                    if pair[1] > j:
                        result.append([array[i], array[j], array[pair[0]], array[pair[1]]])
    return result

@timed(1)
def fourNumberSum2(array, targetSum):
    allPairSums = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k], array[i]]]
            else:
                allPairSums[currentSum].append([array[k], array[i]])
    return quadruplets


array = [7, 6, 4, -1, 1, 2]
targetSum = 16
array2 = [1, 2, 3, 4, 5]
targetSum2 = 100
big_array = [i for i in range(17, 1_000)] + array + [i for i in range(17, 1_000)]
big_array2 = [i for i in range(101, 3_000)] + array2 + [i for i in range(101, 3_000)]
array_worst_case = [i for i in range(-10, 0)] + [i for i in range(1, 11)]
targetSumWorstCase = 0

# fourNumberSum(array, targetSum)
# fourNumberSum2(array, targetSum)
# fourNumberSum(big_array2, targetSum2)
# fourNumberSum2(big_array2, targetSum2)
fourNumberSum(array_worst_case, targetSumWorstCase)
fourNumberSum2(array_worst_case, targetSumWorstCase)