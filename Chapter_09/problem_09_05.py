def transpose_list(two_dimensional_list) :
    return [row for row in zip(*two_dimensional_list)]  # list 안의 tuple로 나옴 [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))