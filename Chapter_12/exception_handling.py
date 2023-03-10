# 예외란 프로그램을 개발하면서 예상하지 못한 상황이 발생하는 것
    # ex) 사용자의 오류 입력, 자동저장 기능
# 예외는 크게 예측 가능한 예외와 예측 불가능한 예외 두 가지가 있음
    # 1. 예측 가능한 예외
        # 발생 여부를 개발자가 사전에 인지할 수 있는 예외
            # ex) 텍스트 박스에 사용자가 실수로 잘못된 값을 입력하는 경우
            # ex) 사용자가 실제로 존재하지 않는 파일에 저장하는 경우
    # 2. 예측 불가능한 예외
        # 대표적으로 매우 많은 파일을 처리할 때 문제가 발생할 수 있음
            # 이런 예측 불가능한 예외가 발생했을 경우, 인터프리터가 자동으로 예외를 사용자에게 알려줌
            # 대부분은 이런 예외가 발생하면서 프로그램이 종료
                # 적절한 조치 필요
# 예외 처리는 제품의 완성도를 높이는 차원에서 매우 중요한 개념
    # 예외의 종류
        # IndexError : 리스트의 인덱스 범위를 넘어갈 때
        # NameError : 존재하지 않는 변수를 호출할 때
        # ZeroDivisionError : 0으로 숫자를 나눌 때
        # ValueError : 변환할 수 없는 문자나 숫자를 변환할 때
        # FileNotFoundError : 존재하지 않는 파일을 호출할 때

# 예외 처리 구문
    # 1. try - except문
        # try : 예외 발생 가능 코드
        # except 예외 타입 : 예외 발생 시 실행되는 코드

for i in range(10) :
    try :
        print(10 / i)
    except ZeroDivisionError as e : # 예외 에러 메세지(division by zero)
        print(e)                    # 특정한 에러를 빠르게 이해할 수 있도록 도와줌
        print("Cannot divide by 0")

    # 2. try - except - else문
        # try : 예외 발생 가능 코드
        # except 예외 타입 : 예외 발생 시 실행되는 코드
        # else : 예외가 발생하지 않을 시 실행되는 코드

for i in range(10) :
    try :
        result = 10 / i
    except ZeroDivisionError as e :
        print(e)    # division by zero
        print("Cannot divide by 0")
    else :
        print(result)

        # 에러가 발생하지 않을 경우의 수행문을 정의함
            # 에러가 명확히 발생하지 않을 경우 사용자가 일어날 일을 예측 가능
                # ex) 서버의 상태가 불안해 연결 끊김이 자주 발생할 경우 해당 코드를 명확히 해 수행하도록 할 수 있음
        # 일반적으로 많이는 사용하지 않는 코드
    
    # 3. try - except - finally문
        # try : 예외 발생 가능 코드
        # except 예외 타입 : 예외 발생 시 실행되는 코드
        # finally : 예외 발생 여부와 상관없이 실행되는 코드

for i in range(10) :
    try :
        result = 10 / i
    except ZeroDivisionError as e :
        print(e)    # division by zero
        print("Cannot divide by 0")
    finally :   # for문 안에 finally 구문이 있다면 finally도 반복되어 실행되는 것에 유의
        print("%d차 작업 종료, 결과값 : %f" % (i + 1, result))

    # 4. raise문
        # try - except와 달리 필요할 때 예외를 발생시키는 코드
        # raise 예외 타입(예외 정보)

while True :
    value = input("변환할 정수 값을 입력해 주세요 :")
    for digit in value :
        if digit not in '0123456789' :
            raise ValueError("정수값을 입력하지 않았습니다.")   # 사실 다른 예외 타입이 들어가도 코드는 돌아감
    print(f"정수값으로 변환된 수 : {int(value)}")

    # 5. assert문
        # 다른 파일에 정리했음