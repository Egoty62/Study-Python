# 웹에서 데이터 다운로드 하기
import urllib.request   # urllib 모듈 호출
url = "URL_주소_입력"

print("다운로드 시작")

fname, header = urllib.request.urlretrieve(url, 'filename.zip')
# urlretrieve() 함수 호출(URL주소, 다운로드 파일명)
    # 결과값으로 다운로드한 파일명과 header 정보를 언패킹

print("다운로드 종료")

# 특정 그림이나 강의자료 같은 데이터를 자동화하여 다운로드 할 때 유용
    # ex) 구글 검색을 통해 특정 인물의 사진만 다운로드 할 수 있는 프로그램