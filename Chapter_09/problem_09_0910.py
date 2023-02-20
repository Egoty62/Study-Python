# 09_09 : 2개 이상 행렬을 더하는 코드 만들기
# 09_10 : 2개 이상의 벡터를 빼는 코드 만들기
def matrix_addition(matrix_1, matrix_2, *args) :
    return(list([[sum(i) for i in zip(*t)] for t in zip(matrix_1, matrix_2, *args)]))

def vector_subtraction(vector_1, vector_2, *args) :
    return(([a - b - sum(i) for a, b, *i in zip(vector_1, vector_2, *args) ]))

print(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]], [[1, 1], [1, 1]] ))

print(vector_subtraction([1, 3], [2, 4], [5, 6], [1, 1]))
# 1 2 5
# 3 4 6