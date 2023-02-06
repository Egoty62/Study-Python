# 기존 리스트형을 사용하여 간단하게 새로운 리스트를 만들
# for문, list를 한 줄에 사용할 수 있음

# 일반적인 반복문 + 리스트
list_for = []
for i in range(10) :
    list_for.append(i)
print(list_for)

# 리스트 컴프리헨션
list_comprehension = [i for i in range(10)]
print(list_comprehension)
# 0으로만 된 리스트를 만들고 싶으면 [0 for i in range(n)]

# if를 사용한 필터링
list_if_1 = [i for i in range(10) if i % 2 == 0]    # (if i % 2 == 0 : list.append(i))
# [0, 2, 4, 6, 8]
list_if_2 = [i if i % 2 == 0 else 0 for i in range(10)] # if 조건에 만족하지 않을 때, else로 다른 값을 할당하여 리스트에 넣을 수 있음
# [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]

# list_if_3 = [i for i in range(10) if i % 2 == 0 else 10] => else가 있으면 무조건 앞에
# list_if_4 = [i if i % 2 == 0 for i in range(10)] => if만 있으면 앞에 두면 안 됨
print(list_if_1, "\n", list_if_2)

# 중첩 반복문 (if를 사용한 필터링 가능)
fruit_1 = ['apple', 'plum', 'lime']
fruit_2 = ['lime', 'lemon', 'grape']
list_nested = [i + j for i in fruit_1 for j in fruit_2]
print(list_nested)  # ['applelime', ... , 'limegrape']

list_if_nested_1 = [i + j for i in fruit_1 for j in fruit_2 if not (i == j)]  # 필터링
list_if_nested_2 = [i + j if not (i == j) else 0 for i in fruit_1 for j in fruit_2]
print(list_if_nested_1) # 위에서 'limelime'만 제외됨
print(list_if_nested_2) # 'limelime'위치에 0이 들어감

# 이차원 리스트 (대괄호를 하나 더 사용)
fruit_3 = ['apple', 'plum', 'lime', 'lemon', 'grape']
list_twoD_1 = [[f.upper(), f.lower(), len(f)] for f in fruit_3]
print(list_twoD_1)
list_twoD_2 = [[i + j for i in fruit_1] for j in fruit_2]
print(list_twoD_2)
# [i + j for i in case_1 for j in case_2]는 일차원 리스트 (i가 기준)
# [[i + j for i in case_1] for j in case_2]는 이차원 리스트 (j가 기준)
# 대괄호의 차이, 위치에 따라 반복의 순서가 달라지는 것에 유의