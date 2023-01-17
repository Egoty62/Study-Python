# 지역 변수와 전역 변수
# 지역 변수는 전역 변수에 영향을 주지 않음

def f() :
    s = "local variable"    # 함수 안에서만 작용하는 지역 변수
    print(s)

def g() :
    global s                # 전역 변수 선언(함수 안에서지만 함수 밖의 변수 s와 같은 메모리 주소를 사용)
    s = "global variable"
    print(s)

s = "variable"              # 함수 안의 s와는 전혀 다른 메모리 주소를 가진 변수

f()                         # f함수와 g함수 실행 순서를 바꾸면 결과가 완전히 달라짐
print("after f() :", s)

g()                         # 함수 실행 목적이 아닌 지식 습득 목적이므로 이렇게 작성함
print("after g() :", s)