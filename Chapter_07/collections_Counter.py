from collections import Counter     # 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환

# 리스트나 문자열과 같은 시퀀스 자료형 안의 값 중 같은 것이 몇 개 있는지 반환
# 기존 사칙연산 및 AND, OR 연산 지원

print("\nCounter 모듈\n")

text_sentence = list("hello world my favorite fruit is lime")
print(text_sentence)
c = Counter(text_sentence)
print(c)    # 개수가 가장 많은 항목 순서대로 출력함
print(c['i'])

text = "hello world my favorite fruit is lime".lower().split()  # 단어 카운팅도 가능
print(Counter(text))

d = Counter({'lime' : 5, 'lemon' : 2})  # 설정할 때는 중괄호 사용(딕셔너리 자료형)
# d = Counter(lime = 5, lemon = 2) 로도 설정 가능 (키워드 형태의 매개변수 사용, 이름을 키로, 실제 값을 값으로)
print(d)
print(list(d))  # ['lime', 'lemon']
print(list(d.elements()))   # ['lime', 'lime', 'lime', 'lime', 'lime', 'lemon', 'lemon']

e = Counter(a = 4, b = 2, c = 0, d = -2)    # list(e.elements())에서는 c, d가 표기가 안 됨
f = Counter(a = 1, b = 2, c = 3, d = 4)
g = Counter(a = 2, b = 3, c = -1, d = 1)

e.subtract(f)   # 변수에 영향을 미침(반환하는 함수가 아님)
print(e)

print(f + g)    # (더하기) Counter({'b': 5, 'd': 5, 'a': 3, 'c': 2})
print(f & g)    # (교집합) Counter({'b': 2, 'a': 1, 'd': 1})
print(f | g)    # (합집합) Counter({'d': 4, 'b': 3, 'c': 3, 'a': 2})