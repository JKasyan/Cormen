import math


def binary_search(array, value):
    searched_position = -1
    current_pos = len(array) - 1
    min_pos = 0
    max_pos = len(array) - 1
    n = 0
    while True:
        if array[current_pos] == value:
            searched_position = current_pos
            break
        elif value > array[current_pos]:
            min_pos = current_pos
        else:
            max_pos = current_pos
        current_pos = (min_pos + max_pos) // 2
        n += 1
    print('n ~ ', n)
    return searched_position


ar = list(range(0, 100))
print('log2n ~ ', math.log(len(ar), 2))
pos = binary_search(ar, 22)
print(pos)
