matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11, 12]]


def force_brute_multiple_matrix(a, b):
    result = []
    rows_number = len(a)
    columns_number = len(b)
    i = 0
    while i < rows_number:
        row = a[i]
        row_res = []
        for k in range(0, rows_number, 1):
            s = 0
            for j in range(0, columns_number, 1):
                s += b[j][k] * row[j]
            row_res.append(s)
        result.append(row_res)
        i += 1
    return result


matrix_c = force_brute_multiple_matrix(matrix_a, matrix_b)
print(matrix_c)

m_1 = [k[0] for k in matrix_b]
print(m_1)

