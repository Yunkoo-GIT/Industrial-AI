print("성적처리 프로그램")
print("=================")

#전체 인원수
number=10 

#리스트 선언
student_name = []   
student_no = []
natlang_score = []
math_score = []
eng_score = []
total_score = []
avg_score = []
grade = []

#데이터 입력
print("입력하세요")
print("-----------------------")
for i in range(number) :
    student_name.append(str(input("학생이름 : ")))
    student_no.append(str(input("학번 : ")))
    natlang_score.append(int(input("국어점수 : ")))
    math_score.append(int(input("수학점수 : ")))
    eng_score.append(int(input("영어점수 : ")))
    print("-----------------------")
    
    total = natlang_score[i] + math_score[i] + eng_score[i]
    total_score.append(total)
    avg_score.append(round(total/3,2))  #소수점 2자리까지

#등수 계산
for i in range(number) :
    rank = 1
    for j in range(number):
        if total_score[i] < total_score[j]: rank += 1
    grade.append(rank)

#줄바꿈
print("\n\n")

#데이터 출력
print("성적처리 결과")
print("================================")
print("학생이름     학    번     국어점수     수학점수     영어점수     총    점     평    균     등    수")
print("===================================================================================================")
for i in range(number) :
    for j in range(number) :
        if grade[j] == i+1 :
            #세로 출력
            #print("학생이름 : ", student_name[j])
            #print("학    번 : ", student_no[j])
            #print("국어점수 : ", natlang_score[j])
            #print("수학점수 : ", math_score[j])
            #print("영어점수 : ", eng_score[j])
            #print("총    점 : ", total_score[j])
            #print("평    균 : ", avg_score[j])
            #print("등    수 : ", grade[j])
            #print("================================")

            #가로 출력(간격  맞추기 어려움)
            print(student_name[j], "     ", student_no[j], "        ", natlang_score[j], "        ",
                  math_score[j], "        ", eng_score[j], "        ", total_score[j], "        ",
                  avg_score[j], "        ", grade[j])
    
