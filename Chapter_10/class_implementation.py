# 클래스 예약어, 클래스 이름(상속받는 객체명)
# 먼저 예약어인 class 작성 후 만들고자 하는 클래스 이름을 작성
# 괄호 안에는 상속받아야 하는 다른 클래스의 이름을 작성
# 파이썬에서 자주 사용하는 작명 기법은 2가지가 있음
# snake_case : 띄어쓰기 부분에 '_' 추가
# CamelCase : 띄어쓰기 부분에 대문자를 사용

class MechanicalEngineering_Score(object) :
    def __init__(self, name, statics = 0, dynamics = 0, fluid_mechanics = 0, thermodynamics = 0, mechanics_of_materials = 0) :
    # self 변수는 클래스에서 생성된 인스턴스에 접근하는 예약어
    # 일단 생성된 인스턴스를 지정하는 변수라고 생각
    # self 뒤의 매개변수들은 실제로 클래스가 가진 속성으로, 실제 생성된 인스턴스에 할당됨
        self.name = name
        self.statics = statics  # 할당되는 코드들
        self.dynamics = dynamics    # 딕셔너리 자료형과 비슷한 형태
        self.fluid = fluid_mechanics    # 생성된 인스턴스에 있는 fluid 변수에 매개변수로 입력된 fluid_mechanics라는 값을 할당
        self.thermo = thermodynamics    # 클래스의 변수는 'self.변수이름'으로, init 함수에서 자유롭게 생성 가능
        self.materials = mechanics_of_materials

# 파이썬은 인터프리터 언어, 동적 타이핑 언어이므로 클래스 내 다른 함수에서도 이 같은 속성의 생성은 가능
# 그러나 일반적으로 __init__() 내에서만 새로운 속성을 생성해야 다른 프로그래머가 이 클래스를 쓸 때 헷갈리지 않음

    def change_statics_score(self, new_Score) :
        print("%s의 정역학의 점수를 %d에서 %d로 변경" %(self.name, self.statics, new_Score))
        self.statics = new_Score
        # 기존 함수와 크게 다르진 않지만 self를 반드시 매개변수에 넣어야 함
        # self가 있어야만 실제로 인스턴스가 사용할 수 있는 함수로 선언
    
    def __str__(self) :
        return f"{self.name}의 점수 : 정역학 {self.statics}, 동역학 {self.dynamics}, 유체역학 {self.fluid}, 열역학 {self.thermo}, 재료역학 {self.materials}"
    # 클래스로 인스턴스를 생성했을 때, 그 인스턴스 자체를 print함수로 화면에 출력하면 이게 나옴

# 생성된 클래스를 인스턴스로 호출해 사용하기
Egoty = MechanicalEngineering_Score("Egoty", 60, 72, 35, 45, 90)
# Egoty라는 인스턴스 자체가 클래스에서 self에 할당됨

print(Egoty)
print("초기 점수 :", Egoty.statics, Egoty.dynamics, Egoty.fluid, Egoty.thermo, Egoty.materials)
Egoty.change_statics_score(87)
print(Egoty)
print("최종 점수 :", Egoty.statics, Egoty.dynamics, Egoty.fluid, Egoty.thermo, Egoty.materials)

# 데이터를 변환하거나 데이터베이스에 저장하는 등 만든 코드가 어떤 역할을 해야할 때 좋음
# 리스트와 함수로 각각 만들어 공유하는 것보다 하나의 객체로 생성해 다른 사람들에게 배포하는 것이 더 쉽게 사용 가능
# 코드를 더 쉽게 선언할 수 있음

names = ['apple', 'lime', 'lemon', 'grape']
statics = [32, 45, 51, 66]
dynamics = [55, 61, 82, 31]
fluids = [12, 92, 100, 62]
thermos = [97, 65, 33, 27]
materials = [100, 22, 66, 73]

students = [[name, static, dynamic, fluid, thermo, material] for name, static, dynamic, fluid, thermo, material in zip(names, statics, dynamics, fluids, thermos, materials)]
print(students)
print(students[2])

student_scores = [MechanicalEngineering_Score(name, static, dynamic, fluid, thermo, material) for name, static, dynamic, fluid, thermo, material in zip(names, statics, dynamics, fluids, thermos, materials)]
print(student_scores[3])

# 이차원 리스트로 단순하게 선언할 수 있지만, 객체 지향 프로그래밍의 개념을 적용하면 좀 더 명확히 저장된 데이터를 확인 할 수 있음
# 특히 다른 사람들이 결과를 사용할 때 이 데이터가 무엇을 위한 데이터인지 명확하게 알 수 있음