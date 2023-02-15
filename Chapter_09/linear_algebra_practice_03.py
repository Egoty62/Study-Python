# 전치행렬

matrix_a = [[1, 2, 3], [4, 5, 6]]

matrix_a_transpose = [[i for i in t] for t in zip(*matrix_a)]

# 1. t in zip(*matrix_a)
# 1 4
# 2 5
# 3 6

# 2. i in t => zip(t)로 하면 튜플이 나옴 [[(1,), (4,)], ... ]
# [1, 4]
# [2, 5]
# [3, 6]

print(matrix_a_transpose)

# 행렬의 곱셈

matrix_1 = [[1, 2, 3], [4, 5, 6]]
matrix_2 = [[7, 8], [9, 10], [11, 12]]

matrix_multi = [[sum((a * b) for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_2)] for row_a in matrix_1]

# 1. column_b in zip(*matrix_2)
# 7   9  11
# 8  10  12

# 2. row_a in matrix_1
# [1, 2, 3]
# [4, 5, 6]

# 3. a, b in zip(row_a, column_b)
# 1 7 \n 2 9 \n 3 11
# 1 8 \n 2 10 \n 3 12
# 4 7 \n 5 9 \n 6 11
# 4 8 \n 5 10 \n 6 12

# 4. sum(a * b)
# 58
# 64
# 139
# 154

print(matrix_multi)