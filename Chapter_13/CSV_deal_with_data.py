# 파이썬에서는 기본적으로 파일 객체가 아닌 csv 객체를 이용해 csv 파일 형태의 데이터를 다루기 쉬움
    # 데이터 내부에 콤마가 있다면 split()만으로는 데이터를 나누기 어려움
        # 그래서 일반적으로 데이터를 묶어주기 위해 따옴표 등을 사용
            # 이 경우, 이 전체를 하나의 데이터로 봐야 하는데, 개발자가 직접 코드를 작성하기엔 시간이 좀 걸림
                # 이 때 csv 객체를 이용하면 조금 더 수월하게 csv 데이터를 사용할 수 있음

# import를 사용하여 csv 객체를 불러옴
    # 그 후 reader() 함수를 열어 각 속성(attribute)에 값을 넣으면 됨

# csv 파일은 https://www.data.go.kr/data/15095901/fileData.do 에서 가져옴
    # 해당 파일의 이용허락범위는 '제한 없음'이므로 자유롭게 사용 가능하다고 판단함

import csv
f = open(".\Chapter_13\인천광역시_유동인구_202110.csv", "r")
reader = csv.reader(
    f,                      # 연결할 대상 파일 객체
    delimiter=',',          # 데이터를 분리하는 기준
    # quotechar="",           # 데이터를 묶을 때 사용하는 문자, 해당 csv파일에는 큰따옴표를 사용하지 않았음
    quoting=csv.QUOTE_ALL   # 데이터를 묶는 기준
)
        
f.close()

    # 13행에서 오픈할 파일 객체를 인수로 넘김
    # 14행에서 delimiter라는 각 데이터를 구분하는 기준을 입력
        # 콤마, \t, -, /, ;등을 구분 기호로 넣을 수 있음, 데이터 종류에 따라 사용
    # 15행에는 데이터를 묶는 기준인 quotechar를 작성
        # 때로는 데이터 사이에 콤마처럼 데이터를 나누는 기준 문자열이 들어갈 수도 있음
        # 이러한 데이터들은 묶어야 하는데, ", ', | 등으로 묶어 데이터를 처리함
            # 데이터를 쉽게 묶기 위해서 잘 쓰지 않는 텍스트들이 csv에 사용될 수 있음
    # 16행의 quoting은 데이터를 묶는 기준을 결정(기본 설정은 csv.QUOTE_MINIMAL)
        # csv.QUOTE_ALL : 모든 데이터를 자료형에 상관없이 묶음, 모든 데이터를 문자열형으로 처리
        # csv.QUOTE_MINIMAL : 최소한의 데이터만 묶음, ','같은 데이터가 포함된 데이터만 묶음
        # csv.QUOTE_NONNUMERIC : 숫자 데이터가 아닌 경우만 묶음, 데이터를 읽어올 때 묶이지 않은 데이터는 csv객체에 의해 실수형으로 읽어옴
        # csv.QUOTE_NONE : 데이터를 묶는 작업을 하지 않음

# 데이터를 읽어 올 때는 reader() 함수, 데이터를 쓸 때는 writer() 함수를 사용

bupyeong_data = []
header = []
rownum = 0

with open(".\Chapter_13\인천광역시_유동인구_202110.csv", "r", encoding= 'cp949') as g :    # 한글처리를 위해 cp949
    csv_data = csv.reader(g)    # csv 객체를 이용해 csv_data 읽기

    for row in csv_data :   # 읽어 온 데이터를 한 줄씩 처리
        if rownum == 0 :
            header = row    # 첫 번째 줄은 데이터 필드로 따로 저장
        location = row[6]   # 군or구 필드 데이터 추출
        if location.find(u"부평구") != -1 : # u는 유니코드 문자열을 의미, find() 함수에서 -1은 문자가 없을 때 출력
            bupyeong_data.append(row)   # 군or구가 부평구인 줄만 데이터 추가

        rownum += 1

with open("bupyeong_floating_population_data.csv", "w", encoding= 'utf8') as h :
    writer = csv.writer(h, delimiter= '\t', quotechar= "'", quoting= csv.QUOTE_ALL)
    # csv.writer() 를 사용해 csv파일 만들기, delimiter는 필드 구분자, quotechar는 필드 각 데이터를 묶는 문자, quoting은 묶는 범위
    writer.writerow(header) # 제목 필드를 파일에 작성
    for row in bupyeong_data :  # 데이터를 하나씩 가져옴
        writer.writerow(row)    # 가져온 정보를 리스트에 작성