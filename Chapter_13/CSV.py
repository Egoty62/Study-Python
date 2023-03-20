# CSV(Comma Separate Values) : 콤마(,)를 기준으로 나누어진 값
    # 테이블 데이터라고 불리는 엑셀 형태의 데이터를 텍스트 형태로 다루는 형식
        # 제일 상단에 필드, 헤더, 또는 열 이름이라 부르는 텍스트 데이터가 입력, 각 데이터는 콤마로 나뉘어짐
        # 그 밑에부터는 실제 데이터가 있음, 각 데이터는 콤마로 나뉘어짐
# 데이터의 분류에는 분류 기준이 되는 문자에 따라 TSV(Tab), SSV(Single-blank)등으로 구분
    # 일반적으로 CSV는 이 모든 자료형을 포함한 것을 뜻함(Chatacter-Separated Values)

line_counter = 0
data_header = []
employee = []
customer_USA_only_list = []
customer = None

with open("customer.csv", "r") as customer_data :   # customer.csv라는 파일이 있다는 가정 하에 코드 생성
    while 1 :   # 무한반복 => 도중에 끊어주는 무언가가 필요함
        data = customer_data.readline()
        if not data :
            break   # 끊어줌
        if line_counter == 0 :
            data_header = data.split(",")
        else :
            customer = data.split(",")

            if customer[10].upper() == 'USA' :  # csv파일에서 11번째 항목이 고객이 살고 있는 나라여서 [10]을 함
                customer_USA_only_list.append(customer)
        
        line_counter += 1

print("Header :", data_header)
for i in range(10) :
    print("Data :", customer_USA_only_list[i])
print(len(customer_USA_only_list))

with open("customer_USA_only.csv", "w") as customer_USA_only_csv :
    for customer in customer_USA_only_list :
        customer_USA_only_csv.write(",".join(customer).strip('\n') + "\n")  # 좌우에 있는 줄넘김을 제거하기 위해 strip() 사용