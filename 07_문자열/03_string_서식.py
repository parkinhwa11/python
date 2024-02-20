# 1. 문자열 정의 : 한줄, 여러줄
text1='Python is great!'
text2='Yes, it is.'
text3='It\'s not like any other'
text4='Don\'t walk.'
text5='This is \
contain \
temp'
text6='''apple\n
banana
melon
'''

# 2. 문자열 포맷(서식) 지정
# 1) 포맷코드 '문자열 포맷코드'% (변수들)
#     ' %05d %.2f %s %c ' % ( , , ,)
# print('%s는 %d살 입니다' %('홍길동',20))

# 2) -'문자열 {위치 인덱스}'.format(변수)
#     '{0:s} {2:5d} {1:.2f} '.format(, ,)
# name='kim';age=20
# print('{0}은 {1}살입니다'.format(name, age))
#    -'문자열 {변수}'.format(변수=값)
# print('{name}은 {age}살입니다'.format(name='홍길동', age=20))

# 3) format(변수, '서식' )
#    format(bmi,'.2f')

# 4) f'string : f' {변수} {변수:서식} '
# print(f'{name}은 {age}살입니다.')

# 3. 날짜 출력 포맷
# 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜 /
# 숫자화 but 문자열

# 모듈(module) : 함수나 변수를 모아놓은 파일
from datetime import date, datetime, timedelta #사용하지 않으면 회색
# date 클래스(객체)에서 today() 함수(method)가 소속
td=date.today() # 년월일 출력
print(td,type(td))
print(f'{td.year}년 {td.month}월 {td.day}일')
print(type(td.year))

# method: 메서드, field : 객체의 변수
#20:50:56.969162
#2024-02-16 20:51:20.217349
curr_time=datetime.now().time()
print(curr_time,type(curr_time))
print(curr_time.hour, curr_time.minute, \
      curr_time.second, curr_time.microsecond)

# timedelta() : 날짜 계산
print(td+timedelta(days=3))
print(td+timedelta(weeks=5))

curr_datetime=datetime.now()
print(curr_datetime+timedelta(hours=-1))
print(curr_datetime+timedelta(days=2, hours=4))

# strftime() : 날짜, 시간 서식 지정
print(td.strftime('%Y-%m-%d %H:%M%S'))
print(td.strftime('%y-%m-%d %I:%M%S %p'))
print(curr_datetime.strftime('%y-%m-%d %I:%M%S %p'))
print(td.strftime('%y년%m월%d일 %I:%M%S %p'))

# 4. 문자열 정렬
# 왼쪽 정렬 : <
# 오른쪽 정렬 : >
# 가운데 정렬 : ^
# 공백문자 지정 : -, # 등등 공백 채우기

text='Python is great!'

print('{0:#<20}'.format(text))
print(f'{text:$>20}')
print(f'{text:*^20}')
print(f'{text:-^20}')











