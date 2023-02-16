# 벡터 n개의 크기가 동일한지 확인하는 한 줄 짜리 코드의 함수

def compare_vectors(vector_1, vector_2) :
    print(all([all([row[0] == value for value in row]) for row in zip(vector_1, vector_2)])) # all의 위치에 유의
    # 안 쪽의 all을 통해 list 안에 true 또는 false를 넣어주니까 한 번 더 all을 써야 함

compare_vectors([1, 2, 3], [1, 2, 4])