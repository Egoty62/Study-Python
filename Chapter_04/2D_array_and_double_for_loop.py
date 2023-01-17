kor_score = [49, 80, 20, 100, 80]
mat_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
student_score = [kor_score, mat_score, eng_score]

ave_score = [0, 0, 0, 0, 0] # 배열 초기화 하는 명령어는 zero()
total_score = 0
for i in range(5) :
    for j in range(3) :
        total_score = total_score + student_score[j][i]
    ave_score[i] = total_score / 3
    total_score = 0
print(ave_score)

# i = 0
# for subject in student_score
    # for score in subject
        # ave_score[i] += score
        # i += 1
    # i = 0
# else :
    # a, b, c, d, e = ave_score
    # student_average = [a/3, b/3, c/3, d/3, e/3]
# print(student_average)