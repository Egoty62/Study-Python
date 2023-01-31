from collections import OrderedDict # 순서를 가진 딕셔너리 객체

# 기존의 딕셔너리는 키의 순서와 저장 순서는 서로 관련이 없지만, OrderedDict 모듈에서는 키의 순서를 보장

print("\nOrderedDict 모듈\n")

fruit = OrderedDict()
fruit['apple'] = 50
fruit['lime'] = 100
fruit['lemon'] = 80
fruit['plum'] = 75
fruit['pineapple'] = 60

for k, v in fruit.items() :
    print("Keys : {0}, Values : {1}".format(k, v))
print("\n")

def sort_by_key(t) :
    return t[0]         # return t[1]로 하면 value 기준으로 정렬됨

for k, v, in OrderedDict(sorted(fruit.items(), key = sort_by_key)).items() :    # sorted 안의 코드만 실행하면 이차원 형태로 키와 값이 출력됨
    print("Keys : {0}, Values : {1}".format(k, v))
# 기존의 딕셔너리 변수를 리스트로 추출, sorted() 함수로 키를 기준으로 정렬 후, OrderedDict로 감싸주는 방식
# => 기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리 형태로 관리 가능