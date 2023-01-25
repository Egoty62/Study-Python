import sys

a = 'abcde'

print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))    # 각각의 메모리 크기 출력

print("-----------------")
print(a[0], a[4])   # 문자열은 list와 같이 사용 가능
print(a[-1], a[-3]) # 문자열은 list와 같이 사용 가능

b = "Hello"
c = "World!"

print(b + c)        # b와 c 사이에 띄어쓰기가 없음
print(b + " " + c)  # 띄어쓰기가 됨