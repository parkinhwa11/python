# 짝수 판단
# elif num%2==1:
#     print("홀수")
# 굳이 한 번 더 쓸 필요 없음.
'''
num=int(input("정수 입력 : "))
if num%2==0:
    print("짝수")
else:
    print("홀수")

# 큰 수 출력

num1=int(input("정수1 입력 : "))
num2=int(input("정수2 입력 : "))
num3=int(input("정수3 입력 : "))
if num1>=num2 and num1>=num3:
    max=num1
elif num2>=num3:
    max=num2
else:
    max=num3
print("제일 큰 수 : ",max)


num1=int(input("정수1 입력 : "))
num2=int(input("정수2 입력 : "))
num3=int(input("정수3 입력 : "))
if num1>num2 and num1>num3:
    maxNum=num1
elif num2>num3:
    maxNum=num2
else: #num1이 num3보다 작은 경우
    maxNum=num3
print(f'제일 큰 수 : {maxNum}')


max=0
if a>=b:
    max=a
else:
    max=b

if max>=c:
    pass
else:
    max=c
print(max)

# 도형 선택 후 면적 구하기

shape=int(input("도형 입력(1: 사각형, 2:삼각형, 3:원): "))
if shape==1:
    w1=int(input("가로 입력: "))
    h1=int(input("세로 입력: "))
    print('사각형의 면적= %.2f'%(w1*h1))
elif shape==2:
    w2=int(input("밑변 입력: "))
    h2=int(input("높이 입력: "))
    print('삼각형의 면적= %.2f'%(w2*h2/2))
elif shape==3:
    PI=3.1415
    r=int(input("반지름 입력: "))
    print('원의 면적= %.2f'%(PI*r**2))
else:
    print("잘못 선택했습니다!")
    


# 가위바위보 게임
hong=input("홍길동 입력 : ")
lee=input("이몽룡 입력 : ")
if hong=="가위" and lee=="보" or hong=="바위" and lee=="가위"\
   or hong=="보" and lee=="바위":
    print("홍길동이 이겼습니다")
elif hong==lee:
    print("비겼습니다.")
else:
    print("이몽룡이 이겼습니다")
    
'''

# 컴퓨터와 주사위 놀이하기
# 랜덤숫자 발생

from random import randint
dice_enter=int(input("주사위 눈의 수 입력 (1~6) : "))
com=randint(1,6)
if dice_enter>com:
    print("축하합니다. 이겼어요!")
elif dice_enter==com:
    print("비겼어요!")
else:
    print("컴퓨터가 이겼어요!")

# 컴퓨터 숫자 표시하기-> print(f'com={com}, me={me}')
























    






