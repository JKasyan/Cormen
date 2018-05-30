def shell_sort(ar):
    length = len(ar)
    f = fib(length)
    x = len(f) - 1
    while x > 0:
        k = f[x]
        i = k
        while i < length:
            j = i - k
            key = ar[i]
            while j >= 0 and ar[j] > key:
                ar[j + k] = ar[j]
                j -= k
            ar[j + k] = key
            i += 1
        x -= 1


def fib(n):
    f = []
    a, b = 1, 1
    while a <= n:
        f.append(a)
        a, b = b, a + b
    return f


array = [1, 20, -20, 31, 4, 2, 44, 11, 2, -1, -5]
shell_sort(array)
print(array)