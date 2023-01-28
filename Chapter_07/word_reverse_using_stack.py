word = input("단어를 입력하세요 :")
word_list = list(word)

result = []
for i in range(len(word_list)) :
    result.append(word_list.pop())  # stack의 원리를 이용함 (pop('인덱스 값') : 리스트 안의 변수를 추출하여 반환)

print("입력한 단어 : %s" % word)    # 저번에 배운 % 서식 지정 활용
print("순서가 바뀐 단어 : {answer}".format(answer = ''.join(result)))   # format 함수 활용 (네이밍)