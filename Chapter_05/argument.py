# 인수
# 인수의 종류에는 키워드 인수, 디폴트 인수, 가변 인수, 키워드 가변 인수가 있음

# 키워드 인수
def a(x, y) :
    print("x : {0}, y : {1}".format(x, y))                  # format 함수 사용

print("function a, keyword argument")
a(123, 234)                                                 # 기본적인 형태
a(y = 123, x = 234)                                         # 각각의 함수에 사용되는 변수명을 정확히 기재하면 입력 순서는 상관 없음

# 디폴트 인수
def b(x, y = 123124) :                                      # y 변수에 디폴트 값 지정
    print("x : {0}, y : {1}".format(x, y))

print("function b, default argument")
b(321, 432)
b(543)                                                      # 인수를 하나만 입력해도 y에 디폴트 값이 있어 함수가 실행됨

# 가변 인수
def c1(x, y, *args) :                                       # 매개변수의 개수가 정해지지 않았을 때 사용, 반드시 *를 붙혀야 함
    print("In function :", args)                            # 결과값이 괄호로 묶여 나오는데, 이를 튜플(tuple) 자료형이라고 함
    return x + y + sum(args)                                # 인덱스 활용 가능(args[0], args[1], ...)

print("c1, variable-length arguments : basic")
c1(1, 2, 3, 4, 5)                                           # 1, 2는 각 x, y에 할당되지만, 나머지는 args에 할당됨
print(c1(1, 2, 3, 4, 5))

def c2(*args) :
    x, y, *z = args                                         # 언패킹을 할 때도 값을 가변 인수 형태로 받을 수 있음
    return x, y, z

print("c2, variable-length arguments : unpacking")    
print(c2(1, 2, 3, 4, 5))                                    # (1, 2, [3, 4, 5])

# 키워드 가변 인수

def d(**kyargs) :                                           # 변수명 자체는 중요하지 않지만 반드시 **로 붙혀야 함
    print(kyargs)                                           # 저장되는 값은 딕셔너리 자료형
    print("First value : {first}".format(**kyargs))
    print("Second value : {second}".format(**kyargs))
    print("Third value : {third}".format(**kyargs))

print("d, keyword variable-length arguments")
d(first = "asdf", second = "qwer", third = "zxcv")          # (x, y, z), 함수 내에서 {0}, {1}, {2}와 같이 쓰면 안 됨 (오류 뜸)

# 그냥 값들 (1, 2, 3, 8, 9)은 튜플형 자료로 *args를 사용해야 함
# first = 1, second = 3 <= 이런 자료들은 딕셔너리 자료형으로 **kwargs에 저장됨