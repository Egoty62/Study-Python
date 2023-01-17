a = input("임의의 수를 입력하세요 : ")
b = input("비교할 수를 입력하세요 : ")

strike = 0
ball = 0

value = 0

char = ' '

overlap = []

if a.isdigit() and b.isdigit() :
    if len(a) > len(b) :
        space = len(a) - len(b)
        b = char * space + b
        number = b
    elif len(a) < len(b) :
        space = len(b) - len(a)
        a = char * space + a
        number = a
    else : number = a


    for i in range(len(number)) :
        if a[i] == b[i] :
            strike += 1

    for i in number :
        if i == char : continue
        if i in overlap : continue
        overlap.append(i)
        if number == a :
            value += a.count(i) - abs(a.count(i) - b.count(i))
        else :
            value += b.count(i) - abs(b.count(i) - a.count(i))

    ball = value - strike

    print("같은 숫자가 포함된 횟수 :", value)
    print("숫자와 자릿수가 모두 일치하는 횟수 :", strike)
    print("숫자만 포함되고 자릿수는 일치하지 않는 횟수 :", ball)

else :
    print("정수형의 숫자만으로 입력하여 주십시오.")