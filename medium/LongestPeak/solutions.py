"""
  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.
  A peak is defined as adjacent integers in the array that are strictly
  increasing until they reach a tip (the highest value in the peak), at which
  point they become strictly decreasing. At least three integers are required to
  form a peak.
  For example, the integers  1, 4, 10, 2  form a peak, but the
  integers 4, 0, 10  don't and neither do the integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3
  don't form a peak because there aren't any strictly increasing integers after the 3.
"""
from decorators.SpeedTestWrapper import timed

"""
 Time complexity: O(N),
 Spice complexity: O(N)
"""
@timed(10)
def longestPeak(array: list[int]) -> int:
    peaks = find_peaks(array)
    if len(peaks) == 0:
        return 0
    longest_peak_array = 0
    for peak in peaks:
        longest_peak_array = max(find_peak_length(array, peak), longest_peak_array)
    return longest_peak_array

def find_peaks(array: list[int]) -> list[int]:
    if len(array) < 3:
        return []
    peaks = []
    for i in range(1, len(array) - 1):
        if array[i-1] < array[i] > array[i+1]:
            peaks.append(i)
    return peaks

def find_peak_length(array: list[int], peak: int) -> int:
    peak_length = 1
    for i in range(peak-1, -1, -1):
        if array[i] < array[i+1]:
            peak_length += 1
        else:
            break
    for i in range(peak, len(array) - 1):
        if array[i] > array[i+1]:
            peak_length += 1
        else:
            break
    return peak_length

"""
 Time complexity: O(N),
 Spice complexity: O(1)
"""
@timed(10)
def longestPeak_v2(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx
    return longestPeakLength

@timed(10)
def longestPeak_Refined(array):
    longest_peak = 0
    i = 1

    # Iterate until the second to last element
    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue
        # 2. Expand Left
        # We already know i-1 is smaller, so start checking from i-2
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1

        # 3. Expand Right
        # We already know i+1 is smaller, so start checking from i+2
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx] < array[right_idx - 1]:
            right_idx += 1

        # 4. Calculate Length
        # The indices are currently "one step too far" (failed checks), so we adjust
        current_peak_length = right_idx - left_idx - 1
        longest_peak = max(longest_peak, current_peak_length)

        # 5. Strategic Skip
        # We jump to right_idx because everything between i and right_idx
        # is part of a downward slope and cannot be a peak tip.
        i = right_idx

    return longest_peak

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
print(longestPeak_v2(array))
print(longestPeak_Refined(array))