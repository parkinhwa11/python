# 예외처리 형식
# try:
#     예외발생가능문장들
# except:
#     예외처리
# else:
#     예외발생하지 않은 경우 처리문장들
# finally:
#     예외발생과 상관없이 항상 실행되는 문장들

# 예외처리 광대한 경우
# try:
#     # print(10/0)
#     print('나이'+23+'살')
# except:
#     print("오류발생")

# try:
#     # print(10/0)
#     print('나이'+23+'살')
# except Exception: 최상위 에러가 담당
#     print("오류발생")

# 에러 종류에 따른 구체적인 담당하는 에러 클래스를 이용하여 처리
# 에러종류 명시
# 에러메시지 변수 활용하여 출력 : 에러담당클래스 as 에러메세지변수명

# try:
#     에러발생가능한 문장들
# except 에러담당클래스명 as 에러메시지변수명:
#     에러처리문장들


try:
    print(10/0)
    print('나이'+23+'살')
except ZeroDivisionError as e: # 첫번째 부분만 처리딤
    print("0으로 나눌 수 없다",e)
except TypeError as e:
    print("잘못입력된 형식입니다",e) # 첫번째만 나옴

try:
    num=int(input('숫자입력: '))
    print(num)
except ValueError as e:
    # print("숫자가 아닙니다.",e)
    pass
else:
    num=num+10
    print(num)
    print('오류가 없습니다')
finally:
    print('종료-----')









