# argparse 모듈
    # 저장된 파일을 사용하는 것이 아니라 프로그램을 콘솔 창에서 실행할 때 세팅을 설정하는 방식
        # 거의 모든 콘솔 프로그램은 실행 시점의 설정 기능을 제공
        # 파이썬 인터프리터도 일종의 콘솔 프로그램 => 이러한 종류의 설정 기능 제공
        # 실행 시점의 설정 파일을 커맨드라인 옵션(command-line option)이라고 함
            # python --v 나 python --h를 누르면 도움말 확인 가능
import argparse

parser = argparse.ArgumentParser(description='Sum two integers.')

parser.add_argument('-a', "--a_value", dest= "a", help= "A integers", type= int)
parser.add_argument('-b', "--b_value", dest= "b", help= "B integers", type= int)
# a, b 인수 추가
args = parser.parse_args()  # 입력된 커맨드 라인 인수 파싱

print(args)
print(args.a)
print(args.b)
print(args.a + args.b)