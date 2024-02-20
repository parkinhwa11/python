# Day2 :
# 1. 자료형(Data Type)

# 기본자료형 : 정수(int), 실수(float), 부울(bool), 문자열(str)
# iterative / 집합적 자료 / sequence : 리스트, 딕셔너리, 튜플, 세트

# 1) 진법 변환 함수
# 2진수, 8진수, 16진수, 10진수
# bin(), oct(), hex()
'''
print('bin(123)=',bin(123))
print('bin(0o123)=',bin(0o123))
print('bin(0x123)=',bin(0x123))

print('oct(123)=',oct(123))
print('oct(0o123)=',oct(0b11010111))
print('oct(0x123)=',oct(0x123))

print('hex(123)=',hex(123))
print('hex(0o123)=',hex(0b11010111))
print('hex(0x123)=',hex(0o123))
'''
# 변수의 자료형 : 실행할 때 결정(동적타이핑)
# id(), type()

# 2) 형변환
# int(string), float(string), str(number)

#int(string, base=10)=int(string)
#int(string, base=2), int(string,8), int(string,16)
'''
print(int('123')) #10진수 문자열을 integer로
print("int('1010',2)=",int('1010',base=2)) #10진수 or 2진수->2진수임을 나타냄
print("int('ff',16)=",int('ff',16)) #16진수
print('int(\'123\',8)=',int('123',8)) #8진수
#결과는 10진수로 표현
'''

# print("int('ff')=",int('ff')) ValueError, base는 10진수야
# 에러 : NameError, TypeError, ValueError

# float(string) : 문자열을 실수형으로 변환

print('float(\'13.5\')=',float('13.5'))
print('float(\'13.5\')=',float('13'))

# str(숫자) : 문자열 변환
#print('나이는=%d' % '20')TypeError 발생. 정수-문자 불일치
print('나이는=%d' % int('20'))
#print('나이는='+20) TypeError 문자열과 숫자 연결 불가
print('나이는='+str(20))

#input() 함수 : 키보드로 입력받아서 문자열로 반환
#input(prompt) : prompt는 화면에 표시되는 문자열 의미
'''
name=input('이름은:')
year=int(input('출생연도는:'))
print(f'이름은 {name},나이는 {2024-year}') #year는 문자열이므로 숫자와 연산 불가하므로 형변환

num = input('실수입력: ')
result= float(num) * 10 #int() 사용시, num이 실수형태로 되어 있어서 정수로 바꿀 수 없음.ValueError
print(f'{num}*10={result}')

# 연산자 : *, +
# 문자열 + 문자열 = 두 문자열을 연결
# 문자열 * 숫자 = 문자열을 숫자만큼 생성해서 연결

#SW+> data + algorithm (+ model + prompt engineering)

# 문제1. 두 정수를 입력받아 합계 구하기
num1=int(input('num1:'))
num2=int(input('num2:'))
print("num1 + num2 =",num1+num2) #print(f'{num1} + {num2} = {num1+num2}')
#num1,num2=map(int,input().split()) 
#print(num1+num2)
'''
# 문제2. 몸무게와 키의 값을 입력받아서 BMI 지수 계산
# BMI= 몸무게/키2
# 몸무게(킬로그램) : 80.5
# 키(미터):1.8
# 당신의 BMI :

weight=float(input('몸무게(킬로그램) :'))
height=float(input('키(미터) : '))
bmi=weight/(height*height) # =>height**2
print("당신의 BMI : %.2f" %bmi)

# eval() : 값에 따라 변환






