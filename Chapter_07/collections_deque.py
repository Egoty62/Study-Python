from collections import deque       # 스택과 큐를 지원

# deque는 연결 리스트의 특성을 지원
# 연결 리스트란, 데이터를 저장할 때 요소의 값을 한 쪽으로 연결한 후, 요소의 다음 값의 주소값을 저장해 데이터를 연결하는 기법
# deque 모듈은 메모리의 효율적 사용과 빠른 속도라는 측면에서 유용함

print("\ndeque 모듈\n")

deque_stack_list = deque()
for i in range(5) :
    deque_stack_list.append(i)
print("초기 리스트(스택) :", deque_stack_list)

deque_stack_list.pop()
deque_stack_list.pop()
print("결과(스택) :", deque_stack_list, '\n')

deque_queue_list = deque()  # deque에선 pop(0)과 같은 것은 작동이 안 되지만, appendleft() 함수가 있음
for i in range(5) :
    deque_queue_list.appendleft(i)
print("초기 리스트(큐) :", deque_queue_list)

deque_queue_list.pop()  # appendleft()한 상태에서 pop을 하면 FIFO가 됨
deque_queue_list.pop()
print("결과(큐) :", deque_queue_list, '\n')

deque_rotate_list = deque()
for i in range(5) :
    deque_rotate_list.appendleft(i)
deque_rotate_list.rotate(3) # rotate(i) : deque모듈 리스트 안의 값을 오른쪽으로 i칸씩 옮김
print(deque_rotate_list)
print(deque(reversed(deque_rotate_list)))   # reversed() : 기존 값과 반대되게 만드는 함수

deque_list = deque()
for i in range(5) :
    deque_list.append(i)
deque_list.extend([5, 6, 7])    # 기존 리스트에 쓰던 함수 사용 가능
deque_list.extendleft([-3, -2, -1]) # extendleft() : 괄호 안 리스트의 값을 '순서대로' 기존 리스트의 왼쪽에 추가함
print(deque_list)   # [-1, -2, -3, 0, 1, 2, 3, 4, 5, 6, 7]