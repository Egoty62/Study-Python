# print 함수를 사용하다보면 어떤 형식에 맞춰 결과를 출력해야 할 일이 생기기도 함
# 6, 7행과 같이 출력하면 데이터와 출력 형식을 분류할 수 있고, 데이터를 형식에 따라 다르게 표현할 수 있음

print(1, 2, 3)
print("a" + " " + "b" + " " + "c")
print("%d %d %d" % (1, 2, 3))           # % 서식 지정을 함 "%자료형 % (값)"
print("{} {} {}".format("a", "b", "c")) # format 함수 사용

print("%s" % "stirng")  # 문자열은 %s
print("%c" % 112)   # 문자 1개는 %c (정수를 써도 되지만 유니코드 번역해서 나옴)
print("%d" % 5) # 정수는 %d
print("%f" % 3.141592)  # 실수는 %f
print("%o" % 63)    # 8진수 표현은 %o
print("%x" % 127)   # 16진수 표현은 %x
print("%%") # 그냥 %% 출력

# 여러 형태의 자료형을 한 번에 출력 가능 (튜플형 자료)
print("문자열 %s, 문자 1개 %c" % ("string", "C"))
print("정수 %d, 실수 %f" % (456, 1.414213))
print("8진수 %o, 16진수 %x" % (62, 126))

# 튜플형 자료에 실제 값 말고 변수를 넣어도 됨
number = 3
day = "three"
print("I ate %d apples. And I was sick for %s days" % (number, day))

# format 함수는 "{자료형}".format(인수) 형식으로 씀
age = 23; name = "EgoTy"
print("My name is {1} and I\'m {0} years old.".format(age, name))
print("float {0:.4f}".format(3.1415926)) # 소수점 4번째까지 출력