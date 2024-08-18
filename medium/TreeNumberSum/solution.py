def three_number_sum(array, target_sum):
    array.sort()
    result = []
    if len(array) < 3:
        return
    for i in range(len(array) - 2):
        left_point = i + 1
        right_point = len(array) - 1
        while left_point < right_point:
            current_sum = array[i] + array[left_point] + array[right_point]
            if target_sum == current_sum:
                result.append([array[i], array[left_point], array[right_point]])
                left_point += 1
                right_point -= 1
            elif target_sum > current_sum:
                left_point += 1
            else:
                right_point -= 1
    return result
