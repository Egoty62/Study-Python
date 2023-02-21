# 클래스 예약어, 클래스 이름(상속받는 객체명)
# 먼저 예약어인 class 작성 후 만들고자 하는 클래스 이름을 작성
# 괄호 안에는 상속받아야 하는 다른 클래스의 이름을 작성
# 파이썬에서 자주 사용하는 작명 기법은 2가지가 있음
# snake_case : 띄어쓰기 부분에 '_' 추가
# CamelCase : 띄어쓰기 부분에 대문자를 사용

class MechanicalEngineering_Score(object) :
    def __init__(self, statics, dynamics, fluid_mechanics, thermodynamics, mechanics_of_materials) :
    # self 변수는 클래스에서 생성된 인스턴스에 접근하는 예약어
    # 일단 생성된 인스턴스를 지정하는 변수라고 생각
    # self 뒤의 매개변수들은 실제로 클래스가 가진 속성으로, 실제 생성된 인스턴스에 할당됨
        self.statics = statics  # 할당되는 코드들
        self.dynamics = dynamics    # 딕셔너리 자료형과 비슷한 형태
        self.fluid = fluid_mechanics    # 생성된 인스턴스에 있는 fluid 변수에 매개변수로 입력된 fluid_mechanics라는 값을 할당
        self.thermo = thermodynamics    # 클래스의 변수는 'self.변수이름'으로, init 함수에서 자유롭게 생성 가능
        self.materials = mechanics_of_materials

# 파이썬은 인터프리터 언어, 동적 타이핑 언어이므로 클래스 내 다른 함수에서도 이 같은 속성의 생성은 가능
# 그러나 일반적으로 __init__() 내에서만 새로운 속성을 생성해야 다른 프로그래머가 이 클래스를 쓸 때 헷갈리지 않음