# 파이썬은 기본적으로 사용해야 하는 문자처리, 웹, 수학 관련 등 다양한 내장 모듈을 제공
# 별다른 조치 없이 import 구문 만으로 사용 가능

import random   # 난수 생성 모듈
import time     # 시간과 관련된 모듈
import urllib   # 웹과 관련된 모듈

# 1. random
# 난수 생성
print(random.randint(0, 100))   # 0 ~ 100 사이의 정수 난수를 생성
print(random.random())          # 일반적인 난수 생성

# 2. time
# 시간을 변경하거나 현재 시각을 출력
print(time.localtime())         # 현재 시간 출력

# 3. urllib
# 대표적으로 request 모듈을 사용하면 특정 URL의 정보를 불러올 수 있음
import urllib.request

response = urllib.request.urlopen("https://www.google.com/")    # 해당 주소의 HTML 정보를 가져옴
print(response.read())