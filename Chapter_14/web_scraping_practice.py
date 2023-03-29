# Chapter_14 : Lab 04
# 정규 표현식을 파이썬으로 다루는 방법 배우기
# 교재에 나와있는 주소를 활용
    # http://goo.gl/U7mSQl

import re   # 정규 표현식을 다루는 모듈 (Regular Expression)
import urllib.request

url = 'http://goo.gl/U7mSQl'    # 접속할 웹 페이지
html = urllib.request.urlopen(url)  # 웹 페이지 열기
html_contents = str(html.read())    # 웹 페이지의 내용을 문자열로 가져옴

# ID가 숫자 or 영문 대소문자가 여러 개 있고 그 뒤에 *로 끝나는 특징을 이용
id_result = re.findall(r"[A-Za-z0-9]+\*\*\*", html_contents)
# r-string => 모든 개행 문자를 그대로 출력해줌 => '\'도 출력해줌
# findall(a, b) : b에서 a를 전부 찾음
    # 영문 대소문자 or 숫자가 포함된 문자열, 그 뒤에는 '***'로 끝남

for result in id_result :
    print(result)

# 파일을 자동으로 다운로드 하고 싶으면
# url_list = re.findall(r"(http)(.+)(zip)", html_contents)
# for url in url_list :
    # full_url = "".join(url)   # 출력된 tuple 형태의 데이터를 문자열로 바꿈
    # print(full_url)
    # fname, header = urllib.request.retrieve(full_url, file_name)  # file_name에 다운로드 할 파일명 작성
    # print("End Download")