# 파이썬에서는 이미 작성된 프로그램을 모듈(module) 이라고 함
# import random과 같이 모듈을 이미 사용한 전적이 있음
# 파이썬의 .py 자체가 모듈

# 네임스페이스(namespace)는 모듈 호출의 범위를 지정
    # 1. 모듈 이름에 알리아스(alias)를 생성하여 모듈 안으로 코드를 호출하는 방법
        # as를 통해 모듈의 이름을 다르게 바꿔 사용
            # ex) import numpy as np
    # 2. from 구문을 사용하여 모듈에서 특정 함수 또는 클래스만 호출하는 방법
        # 이 경우에는 함수에 별도의 모듈명을 쓰지 않아도 단독으로 사용 가능
            # ex) from module_example import convert_rad_to_deg
            # ex) 위의 구문을 사용한 경우 아래 코드를 deg = convert_rad_to_deg(rad)로 사용 가능 
    # 3. from 구문 후 import * 를 하여 해당 모듈 안에 있는 모든 사용 가능한 리소스를 호출하는 방법
        # *는 모든 것이라는 뜻도 있다 (unpacking)
        # 이 경우에도 함수에 별도의 모듈명을 쓰지 않아도 사용 가능
            # ex) from module_example import *
            # ex) deg = convert_rad_to_deg(rad)
# 코드의 출처를 명확히 표현하는 것이 좋기 때문에 1번의 방법이 많이 쓰임

import module_example

rad = ''

while type(rad) != float :
    a = input("라디안 단위의 각도를 입력하여 주십시오. :")
    try :
        rad = float(a)
    except ValueError :
        print("올바른 단위를 입력하여 주십시오")

deg = module_example.convert_rad_to_deg(rad)
print("입력하신 {0}라디안은 {1}도 입니다.".format(rad, deg))