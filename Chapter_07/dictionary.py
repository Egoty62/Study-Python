# 딕셔너리 자료형은 중괄호를 사용하여 표현
# 데이터의 유일한 구분자를 키(key)라는 이름으로 검색할 수 있게 함
# 실제 데이터를 값(walue)이라는 이름으로 쌍으로 저장함
# 딕셔너리 변수 = {키 1 : 값 1, 키 2 : 값 2 , 키 3 : 값 3, ...}
# 딕셔너리는 순서를 보장하지 않는 객체

# 값에는 다양한 자료형이 들어갈 수 있음

fruit = {'fruit_1' : 'apple', 'fruit_2' : 'orange', 'fruit_3' : 'lemon', 'fruit_4' : 'lime'}
print(fruit['fruit_4'])

# 재할당 & 데이터 추가

fruit['fruit_1'] = 'pineapple'
fruit['fruit_5'] = 'plum'
print(fruit)

# 딕셔너리의 함수

print(fruit.keys(),'\n', fruit.values())

for k, v in fruit.items() :
    print("Keys : %s \nValues : %s" % (k, v))

print('lime' in fruit.values())