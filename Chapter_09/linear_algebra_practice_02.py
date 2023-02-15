matrix_a = [[1, 1], [1, 1]]
matrix_b = [[1, 1], [1, 1]]

# all() : 괄호 안에 있는 모든 값이 참일 경우에만 True 반환 (and의 조건으로 리슽트나 튜플의 값 비교)
# any() : 괄호 안에 있는 값 중 하나라도 참일 경우에 True 반환 (or의 조건으로 리스트나 튜플의 값 비교)

print(all([row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row])) # True가 8개 => all()이 있으므로 True로 출력

# 1. t in zip(matrix_a, matrix_b)
# [a11, a12]    [b11, b12]
# [a21, a22]    [b21, b22]

# 2. row in zip(*t)
# a11   b11
# a12   b12
# a21   b21
# a22   b22

# 3. value in row
# for를 통해 a와 b에서 각각 value를 한 번씩 가져옴

# 4. row[0] == value
# value를 a의 값(row[0])과 비교

matrix_b = [[2, 2], [2, 2]]
print(([row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row])) # 실제로 True가 4개는 나옴(위의 설명대로)

print(list([all([row[0] == value for value in row]) for t in zip(matrix_a, matrix_b) for row in zip(*t)])) # [[True, False], [True, False], [True, False], [True, False]]
# 25줄 코드와 27줄 코드에서 for문이 돌아가는 순서는 같음 => 리스트가 1차원이냐 2차원이냐 차이