alist = ['a', 'b', 'c']
blist = ['1', '2', '3']
abcd = []

for a, b in enumerate(zip(alist, blist)) :  # a는 int형, b는 tuple
    try :
        abcd.append([b[a]]) # tuple안의 원소는 list임 (2차원 list가 됨)
    except IndexError :
        abcd.append("error")

print(abcd)