C = int(input())

scores = [list(map(int, input().split())) for i in range(C)]

for student_score in scores:
    average = sum(student_score[1:])/student_score[0]
    pass_student = 0
    for score in student_score[1:]:
        if score > average:
            pass_student += 1
    percentage = pass_student/student_score[0] * 100
    print('%.3f%%'%percentage) 
'''
for i in range(C):
    score = list(map(int, input().split()))
    average = sum(score[1:])/score[0]
    pass_student = 0

    for j in range(score[0]):
        if score[j] >= average:
            pass_student += 1
    percentage = pass_student/score[0] * 100
    print('%.3f%%'%percentage) 
'''

###############################
# 생각 과정
# - 입력을 어떻게 받아야하지? 학생수마다 입력 받는 갯수가 달라짐
# - scores에 리스트에 리스트로 담기게 됨
# - scores를 for문을 돌려서 student_score에 리스트 하나씩 빼서 평균 계산
# - 그리고 for문 안에서 pass_student 변수를 0으로 설정한다.
# - 이중 for문으로 student_score의 1번째부터 돌려서 위에서 구한 평균값보다 크면 pass_student에 1을 더합니다. 
# - 마지막으로 비율을 구해서 percentage 변수에 할당하고, 문제에서 말한 출력 기준에 맞춰 출력합니다. 
###############################

