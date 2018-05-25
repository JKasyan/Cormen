def merge_sort(ar, p, r):
    q = (p + r) / 2
    if p < r:
        merge_sort(ar, p, q)
        merge_sort(ar, q + 1, r)
        merge(ar, p, q, r)


def merge(ar, p, q, r):
    left = ar[p:q + 1]
    right = ar[q + 1:r + 1]
    left.append(None)
    right.append(None)
    i = 0  # left
    j = 0  # right
    ran = range(p, r + 1)
    for k in ran:
        print('k ~ ', k)
        if left[i] <= right[j]:
            ar[k] = left[i]
            i += 1
        else:
            ar[k] = right[j]
            j += 1


array = [4, 2, 1, 3]
merge_sort(array, 0, 3)
print(array)
