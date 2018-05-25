def insert_sort(array):
    i = 1
    while i < len(array):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        i += 1


ar = [300, 1, 20, 3, 44, 2, 77]

insert_sort(ar)
print(ar)
