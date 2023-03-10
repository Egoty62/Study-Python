# 5. assert문
    # 미리 알아야 할 예외 정보가 조건을 만족하지 않을 경우 사용
    # assert문은 True, False의 반환이 가능한 함수를 사용하면 됨
        # False가 반환되면 예외 발생
    # assert 예외 조건

def get_binary_number(decimal_number) :
    assert isinstance(decimal_number, int)  # isinstance() : 입력된 값이 뒤에 있는 클래스의 인스턴스인지 확인하는 함수
    return bin(decimal_number)

print(get_binary_number(10))
print(get_binary_number("10"))  # AssertionError