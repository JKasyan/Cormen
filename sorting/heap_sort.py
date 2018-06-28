def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(ar, i):
    l = left(i)
    r = right(i)
    if l < len(ar) and ar[l] > ar[i]:
        largest = l
    else:
        largest = i
    if r < len(ar) and ar[r] > ar[largest]:
        largest = r
    if largest != i:
        temp = ar[largest]
        ar[largest] = ar[i]
        ar[i] = temp
        max_heapify(ar, largest)


def build_max_heap(ar):
    for i in range(len(ar) // 2, -1, -1):
        max_heapify(ar, i)


def heap_sort(ar):
    build_max_heap(ar)
    for i in range(len(ar) // 2, 0, -1):
        a[0] = a[i]
        max_heapify(ar, 1)

a = [1, 20, 2, -1, 30, 7, 4]
a.abc = 1
heap_sort(a)
print(a)