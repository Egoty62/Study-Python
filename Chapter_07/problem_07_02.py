list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2 (list_data) :
    a = set(list_data)
    return(list(a[1:5]))    # set 자료형은 list처럼 쓸 수 없음
print(quiz_2(list_1))