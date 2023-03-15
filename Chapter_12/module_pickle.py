# 파이썬 프로그램을 실행할 때 생성되는 여러 변수와 객체는 순간적으로 메모리에 로딩되었다 프로그램이 종료되면 사라짐
    # 때로는 사용되는 객체를 저장하여 필요할 때 다시 불러야 하는 경우가 있음
        # 이 경우를 프로그래밍 언어에서는 영속화 (Persistence)
            # 필요한 객체를 파일로 저장하여 다시 사용할 수 있게 함

# pickle 모듈은 메모리에 로딩된 객체를 영속화 할 수 있도록 지원
    # 리스트에 들어간 데이터, 클래스의 오프젝트 등을 파일로 저장 후 나중에 사용할 수 있게 만듦
        # 저장해야하는 정보가 많아지고 결과를 나중에 다시 불러 사용할 경우 유용

# pickle은 이미 필요한 형태(바이너리 형태)대로 저장되어있어 훨씬 속도가 빠름
# 하지만 RCE(원격코드실행)공격을 받을 수 있어, 다운받은 pickle 파일을 사용할 때 주의해야 함
# 또한 검증되지 않은 pickle 데이터를 unpicking하게 될 때 임의의 코드가 실행될 수 있음

import pickle

f = open("list.pickle", "wb")   # 파일을 생성할 때 w가 아닌 wb로 열어야 함 => b는 바이너리파일이라는 뜻, 바이너리 파일로 저장되게 함
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)    # dump(a, b) : 객체 a가 파일 b에 저장됨
f.close()

g = open("list.pickle", "rb")   # 파일을 불러올 때도 바이너리 파일이므로 rb를 써야 함
test_pickle = pickle.load(g)
print(test_pickle)
g.close()

# pickle 모듈은 사용자가 직접 생성한 클래스의 객체도 저장함

class Multiply(object) :
    def __init__(self, multiplier) :
        self.multiplier = multiplier
    def multimulti(self, number) :
        return number * self.multiplier
    
multi = Multiply(5)
print(multi.multimulti(10))

f = open("multiply_object.pickle", "wb")
pickle.dump(multi, f)
f.close()

# 클래스를 pickle 하는 것은 같은 파일 안에 있어야 가능
    # 클래스를 다른 파일에서 불러오고 싶으면 해당 모듈을 import 해야 함
# 그냥 파일의 경우 다른 파일에서도 pickle.load()가 가능