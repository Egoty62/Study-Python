# tuple은 소괄호를 사용하여 선언, 리스트와는 다르게 안의 값을 바꿀 수 없음
# 괄호 안의 값을 바꿀 수 없는 리스트

t = (1, 2, 3)       # 선언은 소괄호를 사용하지만, 표현 방식이 리스트와 비슷함
print(t + t, t * 2)
print(t[:1])    # '1,'로 출력됨 => 값이 하나인 튜플을 선언할 경우 t = (1,)로 반점을 사용 

# t[1] = 30 => TypeError : 'tuple' object does not support item assignment