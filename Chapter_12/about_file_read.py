# 파일 : 컴퓨터를 실행할 때 가장 기본이 되는 단위
    # 프로그램을 실행할 때는 늘 파일을 실행해야 함
        # (디렉터리는 파일을 담는 또 하나의 파일, 윈도우에서는 폴더)
# 파일의 종류는 다양하지만, 기본적으로 바이너리 파일과 텍스트 파일이 있음
    # 바이너리 파일(binary file)
        # 컴퓨터만 이해할 수 있는 형태인 이진법 형식으로 저장된 파일
        # 일반적으로 메모장으로 열면 내용이 깨져보임(메모장에서 해석 불가)
        # ex) 엑셀 파일, 워드 파일 등
    # 텍스트 파일(text file)
        # 사람도 이해할 수 있는 형태인 문자열 형식으로 저장된 파일
        # 메모장으로 열면 내용 확인이 가능
        # ex) 메모장에 저장된 파일, HTML 파일, 파이썬 코드 파일 등
        # 텍스트 파일도 컴퓨터가 처리하기 위해 바이너리 형태로 저장됨

# 파일 읽기
    # open() 함수 사용 => f = open("파일명", "파일 열기 모드"), f.close()
        # 파일 열기 모드 => r : 읽기 모드, w : 쓰기 모드, a : 추가 모드(파일의 마지막에 새로운 내용을 추가할 때)

f = open("아는사람 얘기 가사.txt", "r", encoding = "UTF-8") # txt 파일의 문자 인코딩 방식 차이로 인해 python이 인식을 못 함 => UTF-8
contents_1 = f.read()
print(contents_1)
f.close()   # 하나의 파이썬 프로그램이 하나의 파일을 쓰고 있을 때 사용을 완료하면 반드시 해당 파일을 종료해야 함
            # 복수의 파일을 호출하면 에러가 발생

    # with문과 함께 사용
        # with문은 들여쓰기를 사용하여 들여쓰기가 있는 코드에서는 open()함수가 유지됨
            # 들여쓰기가 종료되면 open()함수도 끝남
                # close()함수를 명시적으로 쓰지 않아도 됨
with open("아는사람 얘기 가사.txt", "r", encoding = "UTF-8") as my_file :   # '=' 대신 'as'로 변수명에 할당
    contents_2 = my_file.read()
    print(type(contents_2), contents_2)

    # 한 줄씩 읽어 리스트형으로 반환
        # read() 대신 readlines() 함수를 사용해 한 쭐씩 내용을 읽어와 문자열 형태로 저장
with open("아는사람 얘기 가사.txt", "r", encoding = "UTF-8") as my_file :
    contents_list = my_file.readlines()
    print(type(contents_list), contents_list)

    # 실행할 때마다 한 줄씩 읽어오기
        # read(), readlines() 대신 readline() 사용
            # read, readlines는 파일을 한 번 열면 파일 처음부터 끝까지 모든 파일의 내용을 읽음
            # readline은 호출될 때마다 한 줄씩 읽어오는 특징이 있음
with open("아는사람 얘기 가사.txt", "r", encoding = "UTF-8") as my_file :
    i = 0
    while 1 :
        line = my_file.readline()
        if not line :
            break
        print(str(i) + "===" + line.replace("\n", ""))  # 한 줄씩 값 출력
        i += 1

    # 파일 안 글자의 통계 정보 출력하기
with open("아는사람 얘기 가사.txt", "r", encoding = "UTF-8") as my_file :
    content_3 = my_file.read()
    word_list = content_3.split()
    line_list = content_3.split("\n")

print("총 글자의 수 : {0}".format(len(content_3)))
print("총 단어의 수 : %d" % (len(word_list)))
print(f"총 줄의 수 : {len(line_list)}")