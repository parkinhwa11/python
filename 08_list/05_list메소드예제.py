# 1. 리스트 요소 추가 : append(), insert()
# 1-1 append 이용
# name_list=[]
# for i in range(3):
#     name=input("회원 입력 : ")
#     name_list.append(name)
# print(name_list)
# # 리스트 형식으로 출력 안 되게
# for n in name_list:
#     print(n,end=" ")
# print()
##
#1-1-2
# i=0
# nameList=[]
# while i<10:
#     name=input("회원 입력 : ")
#     nameList.append(name)
#     i+=1
# print(nameList)

#1-1-3  범위 명확하지 않을 경우 i 필요없음.
# nameList=[]
# while True:
#     name=input("회원 입력 : ")
#     if name == 'x':
#         break
#     else:
#         nameList.append(name)
# print(nameList)

#1-2 insert 이용
# name_list=[]
# for i in range(3):
#     name=input("회원 입력 : ")
#     name_list.insert(i,name)
# print(f'회원 명단 : {name_list}')

# 학생 5명 점수 입력받아 총점/평균 구하기
# 1) 반복문만 사용, 데이터 저장 안 됨
# total=0
# for i in range(5):
#     score = int(input(f'학생{i + 1} 점수 입력 : '))
#     total+=score
#     avg=total/5
# print("총점:",total, " 평균:",avg)

# 2) 리스트 사용
# score_list=[]
# total=0
# for i in range(5):
#     score=int(input(f'학생{i+1} 점수 입력 : '))
#     score_list.append(score)
# for j in score_list:
#     total+=j
# avg=total/len(score_list) # 리스트가 변동될 수 있으니까
# print(f'총점:{total}')
# print(f'평균:{avg}')

# 총점/평균 + 80점 이상인 학생 수 출력
# score_list=[]
# total=0
# for i in range(5):
#     score=int(input(f'학생{i+1} 점수 입력 : '))
#     score_list.append(score)
# cnt=0
# for score in score_list:
#     total+=score
#     if score >= 80:
#       cnt += 1
# avg=total/len(score_list)
# print(f'총점:{total}')
# print(f'평균:{avg}')
# print(f'80점 이상인 학생 수 : {cnt}명')






