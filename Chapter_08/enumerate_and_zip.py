# enumerate() : 리스트의 값을 추출할 때 인덱스를 붙여 함께 출력하는 함수
# enumerate는 주로 딕셔너리형 (인덱스가 키, 리스트 원소가 값)
a_fruit = ['apple', 'lime', 'lemon', 'plum', 'peach']
for k, v in enumerate(a_fruit) :
    print(k, v)

print({i:j for i, j in enumerate(a_fruit)}) # 보통 딕셔너리형

# zip() : 1개 이상의 리스트값이 같은 인덱스에 있을 때 병렬로 묶는 함수
b_fruit = ['grape', 'orange', 'pear', 'melon', 'mango']

for a, b in zip(a_fruit, b_fruit) :
    print(a, b)

print([a + b for a, b in zip(a_fruit, b_fruit)])    # 다양한 방식으로 출력 가능 (책에서는 int자료형 리스트에 sum(x)넣음)

# enumerate()와 zip()함수를 같이 사용할 수 있음
for i, (a, b) in enumerate(zip(a_fruit, b_fruit)) : # a, b는 str자료형
    print(i, a, b)

for i, a in enumerate(zip(a_fruit, b_fruit)) :  # a는 tuple자료형
    print(i, a)