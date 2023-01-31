from collections import defaultdict # 딕셔너리의 변수를 생성할 때 키에 기본 값을 지정

# 새로운 키를 생성할 때 별다른 조치 없이 신규 값을 생성할 수 있음

print("\n defaultdict 모듈\n")

a = defaultdict(lambda : 0) # lambda() 함수는 추후에 공부할 예정 (지금은 return 0으로 생각)
print(a["first"])

fruits = [('apple', 1), ('orange', 2), ('apple', 3), ('orange', 4), ('lime', 1)]  # 이차원 리스트 형태로 저장
b = defaultdict(list)   # 초기값을 리스트로 선언
for k, v in fruits :
    b[k].append(v)

# 같은 이름을 가진 여러 개의 키가 생기는데, defaultdict 모듈은 이런 키의 값들을 하나로 만들 때 사용
print(b.items())    # dict_items([('apple', [1, 3]), ('orange', [2, 4]), ('lime', [1])])