# 디렉터리 만들기
    # 파이썬으로는 파일 뿐만 아니라 디렉터리도 다룰 수 있음
        # os모듈을 사용하면 디렉터리를 쉽게 만듦

import os

# os.mkdir("log")
    # 프로그램 대부분이 새로 실행되므로 기존에 해당 디렉터리가 있는지 확인하는 코드 필요
        # os.path.isdir
if not os.path.isdir("log") :   # 파일이 이미 존재하면 FileExistsError 발생
    os.mkdir("log")             # [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'log'

    # 로그 파일 만들기
        # 프로그램이 동작하는 동안 여러 가지 중간 기록을 하는 파일
            # ex) 웹 프로그램의 경우 외부 접속자의 접속 기록이나 접속 시간 등을 저장하는 파일

if not os.path.exists("log/count_log.txt") :
    f = open("log/count_log.txt", "w", encoding = 'utf8')
    f.write("기록 시작")
    f.close()

with open("log/count_log.txt", "a", encoding = "utf8") as f :
    import random, datetime         # 들여쓰기 안에서도 import가 가능
    for i in range(1, 11) :
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + "값 생성" + "\n"
        f.write(log_line)