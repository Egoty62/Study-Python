class Person(object) :
    def __init__(self, name) :
        self.name = name
    
    def show_info(self) :
        print("이름 : {}".format(self.name))
    
class Researcher(Person) :
    def __init__(self, name, degree) :
        Person.__init__(self, name)     # super 함수를 쓰지 않아도 됨
        self.degree = degree

    def show_info(self):
        Person.show_info(self)          # super 함수를 쓰지 않아도 됨
        print("학위 : {}".format(self.degree))

if __name__ == '__main__' :
    researcher_a = Researcher('a', "석사")
    researcher_b = Researcher('b', '박사')
    researcher_a.show_info()
    researcher_b.show_info()