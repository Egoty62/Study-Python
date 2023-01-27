a = 'abcd e f g'
b = a.split()   # [abcd, e, f, g]
c = (a[:3][0])  # 'abc' => 'a'
d = (b[:3][0][0])   # [abcd, e, f] => 'abcd' => 'a'

print(c + d)    # 'aa' => 문자열의 행렬은 주의깊게 생각하자