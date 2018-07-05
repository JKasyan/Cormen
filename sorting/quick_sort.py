from sorting.utils import exchange


def partition(ar, p, r):
    piv = ar[r]
    i, j = p - 1, p
    while j < r:
        if ar[j] < piv:
            i += 1
            exchange(ar, i, j)
        j += 1
    exchange(ar, i + 1, j)
    return i + 1


def quick_sort(ar, p, r):
    if p < r:
        q = partition(ar, p, r)
        quick_sort(ar, p, q - 1)
        quick_sort(ar, q + 1, p)


array = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(array, 0, len(array) - 1)
print(array)
