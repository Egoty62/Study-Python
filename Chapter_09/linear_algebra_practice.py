matrix_1 = [[3, 6], [4, 5]]
matrix_2 = [[5, 8], [6, 7]]
print(list(zip(matrix_1, matrix_2)))
print([[sum(i) for i in zip(*t)] for t in zip(matrix_1, matrix_2)])

# 1. zip(matrix_1, matrix_2)
# [3, 6]    [5, 8]
# [4, 5]    [6, 7]

# 2. *t (unpacking)
# 3, 6  5, 8
# 4, 5  6, 7

# 3. zip(*t)
# 3 5
# 6 8
# 4 6
# 5 7

# 4. sum(i)
# 8  14  10  12

# 5. [sum(i) for i in zip(*t)]
# [8, 14]   [10, 12]

# 6. [[sum(i) for i in zip(*t)] for t in zip(matrix_1, matrix_2)]
# [[8, 14], [10, 12]]