# 두 가지 방식으로 만들어 봄

print("{0:>6s}".format('*'))
print("{0:>7s}".format('***'))
print("{0:>8s}".format('*****'))
print("{0:>9s}".format('*******'))
print("{0:>10s}".format('*********'))
print("{0:>11s}".format('***********'))

char = ' '
for i in range(6, 12) :
    if i == 11 :
        multi = 0
        print('*' * (2 * (i - 5) - 1))
    else :
        multi = 10 - i
        space = char * multi
        print(space, '*' * (2 * (i - 5) - 1))