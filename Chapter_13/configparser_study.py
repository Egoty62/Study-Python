# logger.setLevel(logging.DEBUG)와 같은 방식으로 코드에 바로 레벨을 지정할 수 있음
    # 하지만 이렇게 레벨을 지정하면 몇 가지 문제점이 발생
        # 1. 사용자가 프로그램을 실행할 때 로깅 레벨을 지정하기 위해 코드를 수정해야 함
            # 다른 사람이 작성한 프로그램을 사용 할 때, 그 때마다 코드를 읽으면서 수정할 곳을 찾아 레벨을 수정해야 함
        # 2. 설정값이 너무 많아질 수 있음
            # 만약 설정값이 10개가 넘는다면 코드 하나하나를 찾아가며 수정하는 것은 거의 불가능

# configparser와 argparse는 설정 저장을 파이썬에서 수행할 수 있도록 지원하는 모듈
    # configparser는 설정 자체를 저장, 실행 시점에 설정이 저장된 파일을 읽어 설정을 적용
    # argparse는 실행 시점의 설정 변수를 직접 지정
        # argparse를 더 많이 사용함

# configparser 모듈
    # 프로그램의 실행 설정 값을 특정 파일에 저장하여 사용하는 방식
    # 앞서 배운 딕셔너리와 비슷하게 설정 파일 안에 키와 값을 넣고, 이를 호출하여 사용
        # example.cfg 라는 설정 파일 생성

import configparser

config = configparser.ConfigParser()    # configparser에서 Configparser 객체 생성
print(config.sections())                # section 정보 읽어오기 (읽은 정보가 없어 아무것도 없음)
config.read('Chapter_13\example.cfg')   # 특정 파일 안의 설정 정보 읽어오기
print(config.sections())                # 해당 파일의 section 정보 읽어오기

for key in config['SectionOne'] :       # SectionOne에 있는 키 출력
    print(key)

print(config['SectionOne']["name"])     # SectionOne의 name 출력

# 딕셔너리와 비슷한 개념으로 생각하면 될 듯
# configparser는 간단한 파일을 만들어 설정 정보를 저장하고, 이를 불러올 때 사용
    # 설정 정보가 많고 사용자가 실행 중 자주 바꾸는 설정이 포함된다면 이를 유용하게 사용 가능

