score = int(input("성적 입력 : "))

if score >= 90 :
    grade = 'A'
elif score >= 80 : 
    grade = 'B'
elif score >= 70 : 
    grade = 'C'
elif score >= 60 :
    grade = 'E'
else : 
    grade = 'F'

print("등급은", grade, "입니다.")
