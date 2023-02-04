# split() : 문자열을 분리하여 리스트로 만듦
# => 괄호 안에 기준이 되는 문자를 넣을 수 있음 ex) split("."), split("a")
# join() : 리스트를 결합하여 문자열로 만듦
# => 괄호 안에는 변수(리스트형)를 넣음
# => 함수 바로 앞에 따옴표를 적고, 그 사이에 연결할 문자를 넣음 ex) ' '.join(fruit), '-'.join(colors)

fruit = 'apple, lemon, lime, plum'
print(fruit.split(", ")) # "," + space를 기준으로 문자열을 나누어 리스트로 만듦
a, b, c, d = fruit.split(", ")  # unpacking도 가능
print(a, b, c, d)

another = [a, b, c, d]
result = '.'.join(another)   # set, tuple형도 join함수 사용 가능
print(result)