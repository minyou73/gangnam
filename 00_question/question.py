# ## 학생성적 관리 프로그램
# # 학생들의 성적을 관리하는 프로그램을 작성하세요
# 1. 학생의 이름과 성적을 입력 받아 저장합니다
# 2. 특정 학생의 성적을 조회합니다
# 3. 모든 학생의 평균 성적을 계산 하여 출력합니다
# 4. 성적이 특정 저수 이상인 학생들의 이름을 출력합니다.


list= {}

for i in range(2):
    x = input('이름: ')
    y = input('성적: ')
    list[x]=y

print(list)

print("성적평균: "+ sum(list.values()) / len(list))

# name = input("학생이름:")
# grade = input("학생성적: ")

# for i, j enumerate(name, grade)