# w=7
# h=5
# s=(w*h)/2
# print('넓이는 %.2f'%s)
# pcnt=10.5
# print("전체 면적의 %.3f%%입니다"%pcnt)
# print(format(10,'5d'))

# kor=90
# eng=80
# math=75
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

# space=" "
# star='*'
# # for i in range(5,0,-1):
# #     print(i*star)
# #
# # for i in range(5,0,-1):
# #     for j in range(0,i):
# #         print(star,end="")
# #     print()
#
# # for i in range(5):
# #     for j in range(4-i):
# #         print(space,end="")
# #     for k in range(2*i+1):
# #         print(star,end="")
# #     print()
#
# # s=''
# # num=int(input("십진수 입력:"))
# # while num>0:
# #     a=num%2
# #     num=num//2
# #     s=str(a)+s
# # print(f'이진수는 0b{s}')
#
# # s='파이썬은재미있어요'
# # cnt=0
# # temp=''
# # for ch in s:
# #     if cnt%2==0:
# #         pass
# #     else:
# #         ch='#'
# #     temp+=ch
# #     cnt+=1
# # print(temp)
#
# # from datetime import date,datetime,timedelta
# # t=date.today()
# # print(t,type(t))
# # print(f'{t.year}년 {t.month:02d}월 {t.day}일')
# #
# # curr=datetime.now().time()
# # print(curr,type(curr))
# # print(curr.hour,curr.minute, curr.second,curr.microsecond)
# # print(t+timedelta(days=-1))
# # print(t+timedelta(weeks=1))
# # curr_datetime=datetime.now()
# # print(curr_datetime+timedelta(days=2,hours=4))
# # print(t.strftime('%Y-%m-%d %H:%M:%S'))
# # print(t.strftime('%y-%m-%d %I:%M:%S %p'))
# # print(t.strftime('%y년%m월%d일 %I:%M:%S %p'))
#
# # text='    ham haha hotdog'
# # print(text.lstrip())
# # text2='I like python, i like swimming, i like hotdog'
# # print(text2.split(','))
# # text3='apple banana kiwi'
# # a=text3.split()
# # print(''.join(a))
# # text4='''firstline
# # ..secondline
# # ..thirdline'''
# # print(text4.split('\n'))
# # print(text4.splitlines('\n'))
# # print(text4.split('\n',maxsplit=1))
# # print(text3.center(30,'*'))
# # print(text3.ljust(30,'-'))
#
# # text='Python is a programming language'
# # temp=''
# # for i in text.split():
# #     print(i)
# #     if i=='language':
# #         temp=i.upper()+temp
# #     else:
# #         temp=i+temp
# # print(temp)
#
# # char=input('문자열을 입력하세요:')
# # temp=''
# # for ch in char:
# #     if ch=='s':
# #         ch='$'
# #     else:
# #         pass
# #     temp+=ch
# # print(temp)
#
# # num=input("숫자를 여러개 입력하세요.")
# # for i in range(len(num)):
# #     print(int(num[i])*'\u2665')
#
# # add=lambda x=10,y=30:x+y
# # print(add())
# # print(add(10,50))
# # print(add(y=100,x=20))
# # print(add(19))
#
# # print(tuple(map((lambda x:x+10),[1,2,3,4,5])))
# # print(tuple((1,2,3)))
# # print(tuple("hello"))
# # a=[1,2,3]
# # print(tuple(a))
#
# # t=1,2,'hello'
# # x,y,z=t
# # print(x,y,z,type(z))
# #
# # t2=1,2,3,4,5
# # *a,b,c=t2
# # print(a,b,c)
#
# d={'one':1, 'two':2,'three':3}
# item=d.items()
# print(item,type(item))
# print(list(item))
#
# for item in d.items():
#     print(item,type(item))
#
# for key, value in d.items():
#     print(key,value)
# print(d.get('two'))
# print(d.setdefault('two'))
# print(d.get('two',4))
# print(d.setdefault('two',4))
# print(d.get('four',5))
# print(d.setdefault('four',5))
# print(d)
# print(d.popitem())
# print(d)
# key,value=d.popitem()
# print(key,value,type(key),type(value))
# d['six']=10
# d['ten']=45
# print(d)
# print(d.pop('two'))
# print(d)
# d2=d.copy()
# print(d,id(d))
# print(d2,id(d2))
# d2['four']=4
# print(d,d2)

# a={'one':1,'two':2}
# b={'four':4,'two':5}
# a.update(b)
# print(a)
# print(b)
# print(a,id(a))
# a={}
# print(a,id(a))

# f=['떡볶이','짜장면','라면','피자']
# s=['김치','단무지','피클']
# print(list(zip(f,s)))
# print(dict(zip(f,s)))
#
# d={food:side for food in f for side in s}
# print(d)
#
# stds=['철수','영희','순희']
# std_dic={name:0 for name in stds}
# print(std_dic)
# print(std_dic.items())

# students=[
#     {'name':'홍길동','korean':87,'math':98,'english':88,'science':95},
#     {'name':'이몽룡','korean':92,'math':98,'english':96,'science':98},
#     {'name':'성춘향','korean':76,'math':96,'english':94,'science':90},
#     {'name':'변학도','korean':98,'math':92,'english':96,'science':92},
#     {'name':'박지성','korean':95,'math':98,'english':98,'science':98},
#     {'name':'류현진','korean':64,'math':88,'english':92,'science':92}
# ]
#
# print('{0:6s}{1:4s}{2:>s}'.format("이름","총점","평균"))
# total=0
# for std in students:
#     total=std["korean"]+std["math"]+std["english"]+std["science"]
#     print('{0:4s}{1:4d}{2:7.2f}'.format(std['name'],total,total/4))
#
# dict={}
# while True:
#     voca=input("영어 단어 등록 (종료는 quit) : ")
#     if voca!="quit":
#         if voca in dict:
#             print(f'{voca}는 이미 등록된 단어입니다.')
#         else:
#             meaning = input(f'{voca}의 뜻입력 (종료는 quit) : ')
#             if meaning =='quit':
#                 break
#             else:
#                 dict[voca]=meaning
#     else:
#         break
# print()
#
# while True:
#     search=input("검색할 단어 입력 (종료는 quit) : ")
#     if search != 'quit':
#         if search in dict:
#             print(f'{search}의 뜻은 {dict[search]}입니다.')
#         else:
#             print(f'{search}는 사전에 없는 단어입니다.')
#     else:
#         print()
#         print("종료합니다.")
#         break






### 함수 이용!!
# def reg_wd(dictionary):
#     while True:
#         word = input("영어 단어 등록 (종료는 quit): ")
#         if word.lower() == 'quit':
#             break
#         if word in dictionary:
#             print(f"{word}는 이미 등록된 단어입니다.")
#         else:
#             mean = input(f"{word}의 뜻 입력: ")
#             dictionary[word] = mean
#
# def sch_wd(dictionary):
#     while True:
#         sch_word = input("검색할 단어를 입력 (종료는 quit): ")
#         if sch_word.lower() == 'quit':
#             print("종료합니다.")
#             break
#         if sch_word in dictionary:
#             print(f"{sch_word}의 뜻은 {dictionary[sch_word]}입니다")
#         else:
#             print(f"{sch_word}는 사전에 없는 단어입니다.")
#
# dict={}
# reg_wd(dict)
# sch_wd(dict)

# a=[1,2,3,4]
# # 삭제1
# print(a,id(a))
# a=[]
# print(a,id(a),type(a))

# 삭제2
# b=[10,20,40,50]
# print(b,id(b))
# b=None
# print(b,id(b),type(b))

# 삭제3
# c=[1,2,3]
# print(c)
# del(c)
# print(c,type(c))

# char=['b','B','a','A','z']
# # char.sort()
# char.sort(key=str.lower,reverse=True)
# print(char)

# a=['강감찬','배고파']
# b=[-100,5.5,30]
# a.extend([10,20])
# print(a)
# a.append([10,20])
# print(a)
# a.insert(1,[10,20])
# print(a)
# a.extend(b)
# print(a)
# print(b,id(b))
# b.clear()
# print(b,type(b),id(b))

# table=[[1,2,3,4],[7,8,10],[10,11,12,14]]
# row_n=len(table)
# col_n=len(table)
# for row in table:
#     for col in row:
#         print(col,end=' ')
#     print()
#
# for r in range(row_n):
#     for c in range(col_n):
#         print(table[r][c],end=' ')
#     print()

# n=int(input("학생 수 입력 : "))
# scoreList=[]
# cnt=0
# total=0
# for i in range(n):
#     score=int(input(f'학생{i+1} 점수 입력 : '))
#     scoreList.append(score)
#     total+=score
#     if score>=80:
#         cnt+=1
# avg=total/n
# print(f'총점 : {total}')
# print(f'평균 : {avg}')
# print(f'80점 이상 학생 : {cnt}명')

# n = int(input("학생 수 입력 : "))
# scoreList = list(map(int, input("각 학생의 점수 입력 (공백으로 구분) : ").split()))
# cnt = sum(map(lambda x: x >= 80, scoreList))
# total = sum(scoreList)
# avg = total / n
# print(f'총점 : {total}')
# print(f'평균 : {avg:.2f}')
# print(f'80점 이상 학생 : {cnt}명')
# a=sorted(scoreList)
# print("점수 내림차순 정렬 : ",a)
#
# productList=[]
# while True:
#     product=input("상품 등록 (엔터키 누르면 종료) :")
#     if product=='':
#         break
#     else:
#         productList.append(product)
# p=' '.join(productList)
# print("등록된 상품 : ",p)

# idioms=["개과천선","구사일생","군계일학","무용지물",\
#        "동고동락","유비무환","입신양명","괄목상대",\
#        "막역지우","고장난명"]
# meanings=["잘못을 고치고 옳은 길에 들어섬","죽일 고비를 여러 번 겪으며 살아나다",\
#          "평범한 사람 가운데 뛰어난 사람","아무짝에나 쓸모 없는 것","고통과 즐거움을 함께 한다",\
#          "미리 준비해두면 근심 걱정이 없다","사회적으로 인정받고 출세하여 이름을 세상에 드날림",\
#          "다른 사람의 학식이나 업적이 크게 진보한 것을 말함","생사를 같이 할 수 있는 친밀한 벗",\
#          "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]
#
# print("사자성어 맞추기 게임을 시작합니다")
# print("----------------------------------")
# from random import randint
# n=len(meanings)
# while True:
#
#     r=randint(0,n-1)
#     print(meanings[r])
#     my_answer=input("이말의 사자성어는? : ")
#     if my_answer==idioms[r]:
#         print()
#         print("맞습니다.. 게임을 종료합니다")
#         break
#     else:
#         print()
#         print("틀렸습니다...다시도전 !")
#         print()

def hello():
    print("Hi")

hello()




