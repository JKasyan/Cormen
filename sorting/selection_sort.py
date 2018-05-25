def selection_sort(array):
    i = 0
    min_key = None
    while i < len(array):
        j = i
        while j < len(array):
            if not min_key:
                min_key = j
            elif array[j] < array[min_key]:
                min_key = j
            j += 1
        key = array[i]
        array[i] = array[min_key]
        array[min_key] = key
        i += 1
        min_key = None


ar = [1, 300, 2, 33, 5, -2, 100]
selection_sort(ar)
print(ar)
