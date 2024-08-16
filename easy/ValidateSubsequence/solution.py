from decorators.SpeedTestWrapper import timed

@timed(1)
def isValidSubsequence(array, sequence):
    label, sub_label = 0, 0
    while sub_label != len(sequence):
        if sequence[sub_label] in array[label:]:
            label = array.index(sequence[sub_label], label) + 1
            sub_label += 1
        else:
            return False
    return True

"""
Time complexity: O(n)
Space complexity: O(1)
"""
@timed(1)
def isValidSubsequence2(array, sequence):
    seq_indx = 0
    for i in range(len(array)):
        if array[i] == sequence[seq_indx]:
            if seq_indx == len(sequence) - 1:
                return True
            seq_indx += 1
    return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, -1]
sequence2 = [1, 6, -1, 10]

big_array = [1, 6] + [i for i in range(30, 100_000_000)] + [-1] + [i for i in range(30, 100_000_000)] + [10]

sequence3 =  [1, 6, -1, 5]

isValidSubsequence(array, sequence)
isValidSubsequence2(array, sequence)
print("\n")
isValidSubsequence(array, sequence2)
isValidSubsequence2(array, sequence2)
print("\n")
isValidSubsequence(big_array, sequence2)
isValidSubsequence2(big_array, sequence2)