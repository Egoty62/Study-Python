def add_num(original_list):
    original_list += [1]    # 대괄호가 벗겨져서 들어감(중괄호로 표현해도 상관 X)
    
my_list = [1,2,3,4]
add_num(my_list)
print(set(my_list))