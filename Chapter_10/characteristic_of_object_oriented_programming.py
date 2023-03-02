# 객체 지향 프로그래밍의 특징
# 객체 지향 프로그래밍의 기본 철학에는 실생활을 모델링 한다는 개념이 있기 때문에, 실생활에 존재하는 다양한 개념을 쉽게 ㅡ로그래밍하기 위한 특징이 많음
# 객체 지향 프로그래밍의 특징에는 크게 상속, 다형성, 가시성이 있음


# 1. 상속(Inheritance)

# 부모 클래스에 정의된 속성과 메서드를 자식 클래스가 물려받아 사용하는 것
# class라는 예약어 다음에 clase_name(object)를 입력하는데, 여기서 object가 class_name의 부모 클래스

class Person(object) :  # 먼저 Person 클래스를 생성
    def __init__(self, name, age) : # init함수를 만들어 name과 age에 관한 정보를 입력할 수 있게 함
        self.name = name
        self.age = age

class Korean(Person) :  # Korean 클래스를 만들어 Person 클래스를 상속받게 함
    pass    # 별도의 구현 없이 pass로 클래스만 존재하게 만들고 Korean 클래스의 인스턴스를 생성해 줌

first_korean = Korean("Egoty", 23)  # Korean 클래스는 별도의 생성자가 없지만, Person 클래스가 가진 생성자를 그대로 사용해 인스턴스를 만들 수 있음
print(first_korean.name)    # Korean 클래스는 Person 클래스에서 생성할 수 있는 변수를 그대로 사용할 수 있음

# 일반적으로 상속하면 부모 클래스보다 자식 클래스의 정보가 더 구체화 됨
# 부모 객체에는 일반적인 기능을, 자식 객체에는 상세한 기능을 넣어야 함
# 같은 일을 하는 메서드지만 부모보다 자식 객체가 좀 더 많은 정보를 줄 수 있음 => 부모 클래스의 메서드를 재정의한다

class StaticScore(object) :
    def __init__(self, name, grade, score) :
        self.name = name
        self.grade = grade
        self.score = score

    def about_me(self) :
        print("My name is %s, and my static grade is %s" % (self.name, self.grade))

class StudyStatic(StaticScore) :
    def __init__(self, name, grade, score, time, difficulty) :
        super().__init__(name, grade, score)    # 부모 객체 사용, super()는 상속 관계에서 부모 클래스를 호출하는 함수
        self.time = time    # 속성값 추가
        self.difficulty = difficulty    # 속성값 추가
    # 이러한 함수의 재정의를 overriding이라고 함
    def about_me(self): # 부모 클래스 함수 재정의
        super().about_me()  # 부모 클래스 함수 사용
        print("I spent %s hours studying statics, and I think static's difficulty is '%s'." % (str(self.time), self.difficulty))

    def study(self) :   # 자식 클래스에만 필요한 새로운 함수를 생성할 수도 있음
        print("studying hard")


# 2. 다형성(polymorphism)

# 같은 이름의 메서드가 다른 기능을 할 수 있도록 하는 것
# 위 클래스에서 about_me의 함수를 부모 클래스와 자식 클래스가 서로 다르게 구현했는데, 이것도 일종의 다형성

class Animal(object) :
    def __init__(self, name) :
        self.name = name
    def talk(self) :
        raise NotImplementedError("Subclass must implement abstract method")    # 아직 구현하지 않은 부분이라는 오류를 강제로 발생 가능, 자식 클래스에만 해당 함수를 사용할 수 있게 만듦
    
class Cat(Animal) :
    def talk(self) :
        return ("Meow!")
    
class Dog(Animal) :
    def talk(self) :
        return "Woof!"

animals = [Cat("aaaa"), Cat("bbbb"), Dog("cccc")]
for animal in animals :
    print(animal.name + ' : ' + animal.talk())

# 부모 클래스는 Animal이고, Cat과 Dog는 Animal클래스를 상속
# talk는 각각 두 동물 클래스의 역할이 다름
    # Animal 클래스에서 talk 함수는 NotImplementedError 클래스 호출
# 두 클래스가 내부 로직에서 같은 이름의 함수를 사용하여 결과를 출력하도록 함


# 3. 가시성(visibility)

# 객체의 정보를 볼 수 있는 레벨을 조절하여 객체의 정보 접근을 숨기는 것
# 파이썬에선 가시성이라 하지만, 좀 더 중요한 핵심 개념은 캡슐화(encapsulation)와 정보 은닉(information hiding)
    # 객체의 재사용을 위해 각 객체가 어떤 역할을 하는지 알아야 하지만, 동시에 구현의 세부적인 내용을 모두 알 필요는 없음
    # 객체의 매개변수 인터페이스만 명확히 알면 사용 가능한데, 이러한 개념을 캡슐화라고 함
    # 동시에 필요한 정보는 숨겨야 함. 외부에서 코드 내부를 볼 수 없게 하기 위해 정보 은닉을 적용
# 클래스 간 간섭 및 정보 공유를 최소화 해 개별 클래스가 단독으로도 잘 동작할 수 있게 하기 위해 캡슐화를 사용해야함
    # 각 클래스가 강하게 연결되어 있으면 독립적으로 사용하기 어려움
# 사용자 입장에서는 상세한 내용을 모르더라도 인터페이스를 이해하면 클래스를 쉽게 사용 가능
# 파이썬에서는 이런 개념을 가시성이라는 이름으로 적용

class Product(object) :
    pass

class Inventory(object) :
    def __init__(self) :
        self.__items = []
    def add_new_item(self, product) :
        if type(product) == Product :
            self.__items.append(product)
            print("new item added")
        else :
            raise ValueError("Invalid Item")
    def get_number_of_items(self) :
        return len(self.__items)
    
    @property                       # property decorator(숨겨진 변수 반환)
    def items(self) :               # private variable을 클래스 외부에서 사용하려면 @property를 사용하면 됨
        return self.__items
    
my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory)

# my_inventory.__items    # AttributeError
# '_'가 특수 역할을 하는 예약 문자로 클래스에서 변수로 두 개 붙어, 사용될 클래스 내부에서만 접근 가능(외부에서 호출 X)
# 클래스 내부용으로만 변수를 사용하고 싶으면 '__변수명'형태로 변수 지정(자바에선 private variable이라 함)
    # 가시성을 클래스 내로 한정하면서 값이 다르게 들어가는 것을 막을 수 있음 (정보 은닉)

items = my_inventory.items  # items 함수로 인해 함수로 __items 호출 가능('__items'로는 호출 불가)
# @property를 붙인 함수 이름으로 사용할 수 있음
items.append(Product())
print(items)
print(my_inventory)
print(my_inventory.get_number_of_items())
print(len(items))
# print(len(my_inventory)) => TypeError : object of type 'Inventory' has no len()