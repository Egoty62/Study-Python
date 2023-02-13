# 함수의 가변 인수를 사용할 때 변수명 앞에 별표를 붙임
# 가변 인수(*args)의 자료형은 tuple, 키워드 가변 인수(**kwargs)의 자료형은 dict
# asterisk는 여러 개의 변수를 담는 컨테이너(container)로서의 속성을 부여하기 때문에 여러 변수를 한꺼번에 넣을 수 있음

def asterisk_test01(a, *args) :
    print(a, args)
    print(type(args))

def asterisk_test02(a, **kwargs) :
    print(a, kwargs)
    print(type(kwargs))

asterisk_test01(1, 2, 3, 4, 5, 6)
asterisk_test02(1, b = 2, c = 3, d = 4, e = 5, f = 6)

# 언패킹 기능
def asterisk_test03(a, args) :  # 입력하는 args가 tuple자료형 부터 시작하기 때문에 asterisk를 붙이지 않음
    print(a, *args)             # 대신 변수 앞에 * 를 붙여 언패킹 (tuple을 언패킹)
    print(type(args))

asterisk_test03(1, (2, 3, 4, 5, 6))
asterisk_test01(1, *(2, 3, 4, 5, 6))    # asterisk를 붙임으로 tuple 변수를 언패킹

# 별표 언패킹 예시
a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
data = ([1, 2], [3, 4], [5, 6])
print(*data)

# 별표의 언패킹 기능은 zip함수와 함께 사용할 때 유용함
for i in zip(*([1, 2], [3, 4], [5, 6])) :
    print(i)
    print(type(i))