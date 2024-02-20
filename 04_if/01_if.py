# 조건문

# if문
'''
num=int(input('정수 입력: '))
if num > 10:
    print('10보다 크다')

    
# if~else 문
if num > 10:
    print('10보다 크다')
else:
    pass # 아무것도 수행하지 않을 경우, 아직 결정 못한 경우 pass
#   print('10보다 작거나 같아요')
'''
# 연습문제1. 등록된 아이디와 비번 확인 로그인

ID='flower'
password='1234'
id_enter=input("아이디 입력: ")
pw_enter=input("비밀번호 입력: ")
'''
if id_enter==ID and pw_enter==password:
    print("로그인 성공!")
else:
    print("로그인 실패!")

# 디테일한 방법, 중첩 if문
if ID==id_enter:
    if password==pw_enter:
        print("로그인 성공")
    else:
        print("로그인 실패: 비밀번호가 다르다")
else:
    print("로그인 실패: 아이디가 다르다")

# 중첩 if : if 조건이 만족하는 경우 또 다른 조건에 따라 실행
# if 아래 if가 존재

if ID==id_enter:
    if password==pw_enter:
        print("로그인 성공")
    else:
        print("로그인 실패: 비밀번호가 다르다")
else:
    if password==pw_enter:
        print('로그인 실패: 아이디가 다르다')
    else:
        print("로그인 실패: 아이디와 비밀번호 모두 다르다")
        
# if~ elif~else문 

if ID==id_enter:
    if password==pw_enter:
        print("로그인 성공")
    else:
        print("로그인 실패: 비밀번호가 다르다")
elif password==pw_enter:
    print('로그인 실패: 아이디가 다르다')
else:
    print("로그인 실패: 아이디와 비밀번호 모두 다르다")
    
# 점수 입력(0~100) 받아서 학점 출력
# 90점 이상 A, 80점 이상 B, 70점 이상 C, 60 이상 D, 60미만 F

grade=int(input("점수를 입력하시오: "))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")
'''
# score="A", score="B", score="C", score="D", score="F" 한 후,
# 마지막에 print(score) 해줘도 됨.
# if 90<=grade<=100: 이런 형식으로 해야 110같은 숫자 넣었을 때 정확한 결과 도출 가능.
# 아니면 애초에 if grade>100: score="100 이상의 점수가 입력되었습니다" 로 거르면 됨.





























