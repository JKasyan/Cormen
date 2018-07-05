def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(heap_array, i):
    ar = heap_array['ar']
    l = left(i)
    r = right(i)
    if l < heap_array["heap_len"] and ar[l] > ar[i]:
        largest = l
    else:
        largest = i
    if r < heap_array["heap_len"] and ar[r] > ar[largest]:
        largest = r
    if largest != i:
        temp = ar[largest]
        ar[largest] = ar[i]
        ar[i] = temp
        max_heapify(heap_array, largest)


def build_max_heap(heap_array):
    for i in range(heap_array["heap_len"] // 2, -1, -1):
        max_heapify(heap_array, i)


def heap_sort(ar):
    heap_array = {'ar': ar, 'heap_len': len(ar)}
    build_max_heap(heap_array)
    r = range(len(ar) - 1, 0, -1)
    for i in r:
        t = ar[0]
        ar[0] = ar[i]
        ar[i] = t
        heap_array['heap_len'] -= 1
        max_heapify(heap_array, 0)


# a = [1, 20, 2, -1, 30, 7, 4]
# heap_sort(a)
# print(a)
