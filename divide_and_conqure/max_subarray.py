import sys


def find_max_crossing_sub_array(ar, low, mid, high):
    left_sum = -sys.maxsize
    s = 0
    max_left = mid
    max_right = mid + 1
    for i in range(low, mid, 1):
        s = s + ar[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -sys.maxsize
    s = 0
    for j in range(mid + 1, high, 1):
        s += ar[j]
        if s > right_sum:
            right_sum = s
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_max_sub_array(ar, left, right):
    if left == right:
        return ar[left], left, right
    else:
        mid = (left + right) // 2
        left_sum, min_left, max_left = find_max_sub_array(ar, left, mid)
        right_sum, min_right, max_right = find_max_sub_array(ar, mid + 1, right)
        cross_sum, max_left, max_right = find_max_crossing_sub_array(ar, left, mid, right)
    if left_sum > right_sum and left_sum > cross_sum:
        return left_sum, min_left, max_left
    elif right_sum > left_sum and right_sum > cross_sum:
        return right_sum, min_right, max_right
    else:
        return cross_sum, max_left, max_right


a = [1, 6, 3, 4]
sub_array = find_max_sub_array(a, 0, len(a) - 1)
print(sub_array)
