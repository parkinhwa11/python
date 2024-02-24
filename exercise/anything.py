# w=7
# h=5
# s=(w*h)/2
# print('넓이는 %.2f'%s)
# pcnt=10.5
# print("전체 면적의 %.3f%%입니다"%pcnt)
# print(format(10,'5d'))

kor=90
eng=80
math=75
# total=kor+eng+math
# avg=total/3
# print("총점:",total,", 평균:",format(avg,'5.2f'))
# print("총점:",total,", 평균:",format(avg,'5.2f'),sep='')
#
# print(format(3.141592,'10.3f'))
# print(format(3.141592,'.3f'))
# print('{1:5d}{2:05d}{0:.3f}'.format(kor,math,eng))

# print('국어',kor,'수학',math,'영어',eng,end='====')
# print('국어',kor,'수학',math,'영어',eng,sep="*")
# print(bin(0o123))
# print(bin(0x123))
# print(0x123)
# print(oct(123))
# print(oct(0b11010111))
# print(oct(0x123))
# print(hex(123))
# print(hex(0b11010111))
# print(hex(0o123))

# print('int(\'1010\',base=2)=',int('1010',2))
# print("int('ff',16)=",int('ff',16))
# print("int('123',8)=",int('123',8))
# print("int('ff')=",int('ff'))

# weight=float(input('몸무게:'))
# height=float(input('키:'))
# bmi=weight/(height**2)
# print("{0:.4f}".format(bmi))xs

# a=100
# print(~a)
# print(a<<1)
# print(a>>3)
# print(int('17',8))
# print(oct(12))

# num=input("16진수를 입력하시오: ")
# if "A"<=num<="F" or "a"<=num<="f" or '0'<=num<='9':
#     print("10진수 값은",int(num,16))
# elif num>=2:
#     print("범위 초과하였습니다.")
# else:
#     print("16진수가 아닙니다.")

# for dan in range(2,10):
#     for i in range(1,10):
#         print(f'{dan}*{i:2d}={dan*i:>3}')
#     print()

space=" "
star='*'
# for i in range(5,0,-1):
#     print(i*star)
#
# for i in range(5,0,-1):
#     for j in range(0,i):
#         print(star,end="")
#     print()

# for i in range(5):
#     for j in range(4-i):
#         print(space,end="")
#     for k in range(2*i+1):
#         print(star,end="")
#     print()

# s=''
# num=int(input("십진수 입력:"))
# while num>0:
#     a=num%2
#     num=num//2
#     s=str(a)+s
# print(f'이진수는 0b{s}')

# s='파이썬은재미있어요'
# cnt=0
# temp=''
# for ch in s:
#     if cnt%2==0:
#         pass
#     else:
#         ch='#'
#     temp+=ch
#     cnt+=1
# print(temp)

# from datetime import date,datetime,timedelta
# t=date.today()
# print(t,type(t))
# print(f'{t.year}년 {t.month:02d}월 {t.day}일')
#
# curr=datetime.now().time()
# print(curr,type(curr))
# print(curr.hour,curr.minute, curr.second,curr.microsecond)
# print(t+timedelta(days=-1))
# print(t+timedelta(weeks=1))
# curr_datetime=datetime.now()
# print(curr_datetime+timedelta(days=2,hours=4))
# print(t.strftime('%Y-%m-%d %H:%M:%S'))
# print(t.strftime('%y-%m-%d %I:%M:%S %p'))
# print(t.strftime('%y년%m월%d일 %I:%M:%S %p'))

# text='    ham haha hotdog'
# print(text.lstrip())
# text2='I like python, i like swimming, i like hotdog'
# print(text2.split(','))
# text3='apple banana kiwi'
# a=text3.split()
# print(''.join(a))
# text4='''firstline
# ..secondline
# ..thirdline'''
# print(text4.split('\n'))
# print(text4.splitlines('\n'))
# print(text4.split('\n',maxsplit=1))
# print(text3.center(30,'*'))
# print(text3.ljust(30,'-'))

# text='Python is a programming language'
# temp=''
# for i in text.split():
#     print(i)
#     if i=='language':
#         temp=i.upper()+temp
#     else:
#         temp=i+temp
# print(temp)

# char=input('문자열을 입력하세요:')
# temp=''
# for ch in char:
#     if ch=='s':
#         ch='$'
#     else:
#         pass
#     temp+=ch
# print(temp)

# num=input("숫자를 여러개 입력하세요.")
# for i in range(len(num)):
#     print(int(num[i])*'\u2665')