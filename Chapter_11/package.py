# 패키지(package)는 모듈의 묶음
    # 모듈은 하나의 파일로 이루어져있고, 패키지는 파일이 포함된 디렉터리(폴더)로 구성
# 다른 사람이 만든 프로그램을 불러 사용하는 것을 라이브러리라고 함
    # 파이썬에서는 패키지를 하나의 라이브러리로 이해하면 됨
# 패키지에는 예약어가 있음
    # 패키지에서는 파일명 자체가 예약어를 반드시 지켜야만 실행되는 경우가 있음
        # __init__, __main__, ...

# 교재의 내용을 그대로 따라서 패키지를 만들어 보았음
    # 인터넷에서 주식 정보를 받아와 데이터베이스에 저장하고 필요한 정보를 계산하는 프로그램

# 1단계 : 디렉터리 구성하기
    # 패키지 'roboadviser'(패키지 이름 대부분은 소문자 사용)에는 세 가지 기능이 있음
        # 1) crawling : 주식 관련 데이터를 인터넷에서 가져오는 기능
        # 2) database : 가져온 데이터를 데이터베이스에 저장하는 기능
        # 3) analysis : 해당 정보를 분석하여 의미 있는 값을 뽑는 기능

# 2단계 : 디렉터리별로 필요한 모듈 만들기
    # 하나의 패키지는 중첩된 구조로 만들 수 있음
        # 패키지 안에 또 하나의 패키지가 들어갈 수 있음
        # 각각의 디렉터리를 하나의 패키지로 선언하기 위해서는 __init__.py등의 예약된 파일을 만들어야 함
            # __init__.py 파일은 각 디렉터리가 패키지임을 나타내는 예약파일(이 파일이 없으면 패키지 취급 X)

# 디렉터리가 잘 실행되는 지 테스트
from roboadviser.analysis import series
series.series_test()
# 이런 방식으로 import 하여 코드를 실행하면 roboadviser 디렉터리 안에는 __pycache__ 라는 디렉터리가 생성됨
    # 파이썬의 언어적 특성으로 생기는 결과
    # __pycache__ 디렉터리에는 해당 프로그램이 작동될 때 사용하기 위한 모듈들을 컴파일 후 그 결과를 저장
        # __pycache__ 디렉터리가 한 번 생성되면 그 시점에서 해당 모듈을 수정해도 결과가 반영되지 않음
            # 해당 프로그램이 완전히 종료한 후 수정해야 해당 모듈의 결과 반영 가능

# 3단계 : 디렉터리별로 '__init__.py' 구성하기
    # __init__은 해당 디렉터리가 파이썬의 패키지라고 선언하는 초기화 스크립트
        # 거의 모든 라이브러리에 있음
    # __init__ 파일은 패키지 개발자, 설치 시 확인해야 할 내용 등 메타데이터라 할 수 있는 내용을 담음
    # 일반적으로 이 파일에는 해당 패키지가 포함된 모듈에 관한 정보가 있음
