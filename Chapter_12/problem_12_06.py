sentence = list("Hello Gachon")
while (len(sentence) + 1) : # while문은 조건문이 True일 때 반복실행 되지만, 조건문이 존재할 때에도 실행한다고 생각
    try :
        print(sentence.pop(0))
    except Exception as e :
        print(e)
        break   # break 없으면 while문이 계속 실행되면서 pop from empty list 라는 문구가 계속 나옴