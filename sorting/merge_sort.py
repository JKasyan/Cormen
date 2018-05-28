import sys


def merge_sort(ar, p, r):
    q = (p + r) // 2
    if p < r:
        merge_sort(ar, p, q)
        merge_sort(ar, q + 1, r)
        merge(ar, p, q, r)


def merge(ar, p, q, r):
    left = ar[p:q + 1]
    right = ar[q + 1:r + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i, j = 0, 0
    k = p
    while k <= r:
        if left[i] <= right[j]:
            ar[k] = left[i]
            i += 1
        else:
            ar[k] = right[j]
            j += 1
        k += 1


array = [4, 2, 3, 1, 0, 6, 7]
merge_sort(array, 0, len(array) - 1)
print(array)
