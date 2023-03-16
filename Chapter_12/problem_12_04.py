def sum_data(list_data_a, list_data_b) :
    for i in list_data_a :
        for j in list_data_b :
            result = i + j

        return result   # for문이 반복되지 않고 result라는 값을 반환
        # 함수의 내용물 중간에서 return문이 실행되면 결과값이 반환되며 함수는 중단된다.
        
    
a = [1, 2]
b = [3, 4]
print(sum_data(a, b))