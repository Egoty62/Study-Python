# HTML 파싱
# HTML 코드를 보면 크게 두 가지 부분으로 구성됨을 알 수 있음
    # ~에 정보가 있음
    # ~ 정보를 추출
        # 정규 표현식도 두 가지로 표현 가능
            # (\)([\s\S]+?)(\<\dl>)
                # 이 이후에 여기서 <dd> ~ <\dd> 정보를 추출해야 함
                    # (\)([\s\S]+?)(\<\dd>)
                        # \s는 공백, \S는 문자전체를 의미
                        # +?는 최대한 적게 찾는 기호
                            # 공백 + 문자 전체를 최대한 적게 찾는다는 뜻?

import urllib.request
import re

url = 'https://finance.naver.com/item/main.nhn?code=005930'
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

stock_result = re.findall('(\<dl class=\"blind\"\>)([\s\S]+?)(\</dl\>)', html_contents)

samsung_stock = stock_result[0]     # 두 개의 tuple값 중 첫 번째 패턴   
samsung_index = samsung_stock[1]    # 세 개의 tuple값 중 두 번째 패턴

# 주식 정보만 추출
index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

#for index in index_list :
#    print(index[1])

print(stock_result[1])