# 재귀함수
# 여기서는 팩토리얼 사용

def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)   # 함수 안에 같은 함수를 넣음

print(factorial(int(input("팩토리얼 할 수를 입력하세요 :"))))
# for문이나 while문으로도 똑같이 표현이 가능함