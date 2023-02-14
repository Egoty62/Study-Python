# 맵리듀스는 파이썬 뿐 아니라 빅데이터를 처리하기 위한 기본 알고리즘으로도 많이 사용
# 대용량 데이터를 처리할 맵리듀스의 개념은 매우 유용

# map() 함수는 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용
# 일반적으로 리스트나 튜플처럼 요소가 있는 시퀀스 자료형에 사용됨
# 현재에는 list comprehension으로 대체 가능

m = [2, 4, 6, 8, 10]
f = lambda x : x ** 2
print(list(map(f, m)))  # 제너레이터라는 개념이 강화되면서 list를 붙혀야 list로 반환함
# [x ** 2 for x in m]
print(map(f, m))    # 제너레이터는 시퀀스 자료형의 데이터를 처리할 때, 실행 시점의 값을 생성하여 효율적으로 메모리를 관리할 수 있음

# list를 안 붙히고 출력하는 방법
for value in map(f, m) :    
    print(value)

# 두 개 이상의 시퀀스 자료형 데이터 처리
g = lambda x, y : x + y
print(list(map(g, m, m)))   
# [x + y for x, y in zip(m, m)]

# 리스트 컴프리헨션과 같이 필터링 기능 사용 가능 (else문이 반드시 존재해야 함)
print(list(map(lambda x : x ** 2 if x % 3 == 0 else x, m)))
# [x ** 2 if x % 3 == 0 else x for x in m]

# reduce()는 시퀀스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수
# 값을 차례대로 뽑는다는 것은 map()과 같지만, 리스트 변수의 모든 값을 람다함수로 모두 적용함

from functools import reduce

print(reduce(lambda x, y : x + y, m))

# for 문으로 reduce를 표현한다면
x = 0
for y in m :
    x += y
print(x)