birth = int(input("당신이 태어난 연도를 입력하세요 : "))

age = 2023 - birth + 1

if age <= 26 and age >= 20 : 
    print("당신은 대학생입니다.")
elif age < 20 and age >= 17 : 
    print("당신은 고등학생입니다.")
elif age < 17 and age >= 14 : 
    print("당신은 중학생입니다.")
elif age < 14 and age >= 8 :
    print("당신은 초등학생입니다.")
else :
    print("당신은 학생이 아닙니다.")