# 함수
# 재사용 / 자주 사용하는 기능들을 위한 코드 집합
# 경제적, 관리용이
# 내장함수 / 사용자 정의 함수
# https://docs.python.org/3.12/library/functions.html

# 함수 정의 및 호출

# 이름, 나이, 연락처 출력 함수
def show_info():
    print(f'이름 : 홍길동')
    print(f'나이 : 20')
    print(f'연락처 : 010-1111-1111')

show_info()

# def show_info1():
#     # 나이, 이름, 연락처 입력 받아 출력
#     name=input("이름 입력 : ")
#     age=input("나이 입력 : ")
#     phone=input("연락처 입력 : ")
#     print(name, age, phone)
#
# show_info1()

# 문제. 두 정수를 입력받아 더하는 함수 add() 정의하기
def add(num1,num2):
    print(f'{num1}+{num2}={num1+num2}')
add(1,2)

# 방법2.
# def add():
#     num1=int(input("정수 1 입력: "))
#     num2=int(input("정수 2 입력: "))
#     print(f'{num1},{num2}의 합은 {num1+num2}')
# # result=add() #반환하는 게 없음 None
# add()

# 반환값이 있는 함수 정의
def add2():
    num1 = int(input("정수 1 입력: "))
    num2 = int(input("정수 2 입력: "))
    result=num1+num2
    print(f'{num1},{num2}의 합은 {result}')
    return result
print(f'return value={add2()}') # 반환 값 있음


