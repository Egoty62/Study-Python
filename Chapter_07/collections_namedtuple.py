from collections import namedtuple  # 튜플의 형태로 데이터 구조체를 저장

# 여러 규정된 정보를 하나의 튜플 형태로 구성해 손쉽게 사용할 수 있음
# C언어에서는 struct로 쓰임

Point = namedtuple('Point', ['x', 'y']) # Point 객체의 이름을 Point로 지정, 저장되는 요소의 이름은 x, y
p = Point('11', y = 22)   # 순서 표기 잘 해야함 (11, x = 22)는 불가능
print(p)    # Point(x = 11, y = 22)
print(p.x, p.y) # 변수명과 요소의 이름을 결합시켜 호출 가능
print(p[0] * p[1])  # 인덱스를 이용하여 호출 가능 => 덧셈 연산은 물론 언패킹 연산도 가능