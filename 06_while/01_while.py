# for number in range(1,10):
#     print(number,end=' ')
#
# num=1
# while num<=100:
#     print(num,end=',')
#     num+=1
#     # 무한루프 빠지지 않기 위해 num 1씩 증가해야 함!
#
# 1부터 100 사이 3 배수 합

# total=0
# for i in range(1,101,3):
#     total+=i
# print(total)
#
# sumx=0
# num=3
# while num<=100:
#     if num%3==0:
#         sumx+=num
#     num+=1
# print(sumx)
#
#
# sumx=0
# num=3
# while num<=100:
#     sumx+=num
#     num+=3
# print(sumx)
#
# # 7 입력 시 종료
# n=int(input("숫자 입력 : "))
# while n!=7:
#     n=int(input("다시 입력: "))
# print("7 입력! 종료")
#
# # 연습문제 if 1번 문제: 10진수를 2진수로
#
# dec=int(input("십진수 입력: " ))
# bin_=''
# while dec>0:
#     r=dec%2
#     dec=dec//2
#     bin_=str(r)+bin_
# print('0b'+bin_)

#10진수를 2진수로 변환
dec=int(input("십진수 입력: "))
bin_=""
while dec>0:
    rest=dec%2
    dec=dec//2
    bin_=str(rest)+bin_
print("0b"+bin_)






















