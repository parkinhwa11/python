# # 2번 i만 출력
# num=['12','34','56']
# for i in num:
#     i=int(i)
#     print(i) # 12 34 56 다 출력
# print(i) # 56만 출력

# 3번 반복횟수 확인
# cnt=0
# for i in range(1,100,4):
#     print("파이썬 꿀잼")
#     cnt+=1
# print(f'{cnt}번 출력')

# #5번
# result=0
# for i in range(5,-5,-2):
#     if i<-3:
#         result+=1
#     else:
#         result-=1
# print(result)

# #9번
# coupon=0
# money=200000
# coffee=3500
# cnt=0
# c_cnt=0
# while money>coffee:
#     if coupon<4:
#         money=money-coffee
#         coupon+=1
#     else:
#         money+=2800
#         coupon=0
#         c_cnt+=1 #쿠폰에 해당하는 money 지급
#     cnt+=1 #누적쿠폰수
#     print(f'남은 돈 {money}')#돈 변화
# print(money,cnt,c_cnt)


# #10번
# a=[1,2]
# b=[3,4]
# for i in a:
#     for j in b:
#         result=i+j #result+=i+j, result=result+i+j
#         #앞전에 초기화 안 했기 때문에 에러가 발생한다.
# print(result)

#11-1번
#풀이 1-중첩 for
# star='*'
# for n in range(5,0,-1):
#     for i in range(0,n):
#         print(star,end="")
#     print()

# 풀이 2-문자열 곱하기 연산 가능
# for i in range(5,0,-1):
#     print(star*i)

# 풀이 3-입력받은 숫자만큼 별 생성
# n=int(input("숫자 입력: "))
# for i in range(0,n):
#     print('*'*(n-i))

#11-2번
#풀이1-중첩
# space=' '
# star='*'
# for i in range(5):
#     for a in range(4-i):
#         print(space,end='')
#     for b in range(i*2+1):
#         print(star,end='')
#     print()
#풀이1-1-while
space=' '
star='*'
# i=0
# while i<5:
#     a=0
#     while a<4-i:
#         print(space,end="")
#         a+=1
#     b=0
#     while b<i*2+1:
#         print(star,end="")
#         b+=1
#     print()
#     i+=1
# # while 풀이 2
# i=0
# while i<5:
#     a=4-i
#     b=2*i+1
#     j,k=0,0
#     while j<a:
#         print(space,end="")
#         j+=1
#     while k<b:
#         print(star, end="")
#         k+=1
#     i+=1
#     print()
# # while 풀이 2
# i=0
# while i<5:
#     print(space*(4-i),star*(2*i+1))
#     i+=1
#풀이2
# for i in range(5):
#     print(space*(4-i)+star*(i*2+1))

#풀이3
for i in range(1,10,2):
    print("{0:^10}".format(i*"*"))
#위의 방식은 정렬 방식. 가운데 정렬. ^10
#<왼쪽 정렬, >오른쪽 정렬, ^가운데 정렬

