# 4개 정수입력받아 합계, 평균
# 풀이 1-입력 숫자가 많아지면 늘리기 어려운 한계
# num1=int(input('1번째 숫자: '))
# num2=int(input('2번째 숫자: '))
# num3=int(input('3번째 숫자: '))
# num4=int(input('4번째 숫자: '))
# total=num1+num2+num3+num4
# avg=total/4
# print(f'합계:{total}, 평균:{avg}')

# 풀이2-반복문-입력받은 데이터 저장 불가
# n=10
# sumx=0
# for i in range(n):
#     num=int(input(f'{i+1}번째 숫자: '))
#     sumx+=num
# avg=sumx/4
# print("합계는",sumx, "평균은",avg)
# 데이터가 기억이 안 된다. 마지막 것만 기억함.

# 풀이3-리스트로 해결
# n=4
# sumx=0
# num_list=[] # num_list=list()
# for i in range(n):
#     num=int(input(f'{i+1}번째 숫자 : '))
#     num_list.append(num) # 빈 리스트에 입력받은 num의 숫자들을 하나씩 더해줌.
#     sumx+=num
# avg=sumx/4
# print(f'합계:{sumx}, 평균:{avg}')
# print('num_list=',num_list) #데이터 저장 가능
#
# for num in num_list: # 리스트 데이터 하나하나 확인 가능
#     print(num)

# lists=[1,2,3,[1,3],[5,6,7]]
# print(lists)
# print(lists[0])
# print(lists[-1])

# 리스트 생성 : [], list()
# 리스트 요소 추가 : append()
# 리스트 길이 : len(리스트명)

# aList=list() # aList=[]
# for i in range(10):
#     print(aList)
#     aList.append(i)
# print(aList)

# # for 와 list

# sumx=0
# num_list=[] # num_list=list()
# # 리스트에 입력한 데이터 저장
# for i in range(4):
#     num=int(input(f'{i+1}번째 숫자 : '))
#     num_list.append(num)
# # 리스트 데이터 이용해 계산
# for x in num_list:
#     sumx+=x

    #또는

# for i in range(len(num_list)):
#     sumx+=num_list[i]
# =sumx=num_list[0]+num_list[1]+num_list[2]+num_list[3]

# avg=sumx/4
# print(f'합계:{sumx}, 평균:{avg}')
# print('num_list=',num_list)

# 리스트의 요소 출력
# for i in range(len(num_list)):
#     print(num_list[i])
#
# # 또는
#
# for x in num_list:
#     print(x)
