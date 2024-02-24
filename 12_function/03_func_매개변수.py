# 함수의 매개변수(parameter)와 인수(인자:argument)

# 매개변수 : 함수를 정의할 때 함수로 전달되는 값을 갖는 변수(함수 정의)
# 인수 : 함수를 호출할 때 전달되는 값 (변수)

def get_area(width,height):
    result=width*height
    print(f'사각형 가로={width},세로={height}, 면적은 {result}')
    return result

print(get_area(10,20))

# 문제. 사칙연산을 수행하는 함수 정의
# add() : 두 수 더하기
# sub() mul() div()

# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mul(a,b):
#     return a*b
#
# def div(a,b):
#     if b is 0:
#         print("0으로 나눌 수 없다")
#     else:
#         return a/b
#
# # 전역변수 : 함수 밖에서 정의된 변수
# x=2
# y=3
# add(x,y)
# sub(x,y)
# mul(x,y)
# div(x,y)
# 매개변수와 인수는 다르다!

# 2. 디폴트 매개변수
# 매개변수의 기본값이 지정되어 있는 경우
# 디폴트 매개변수는 마지막에 위치해야 함!

def greet(name, msg):
    print(name+","+msg)

# greet('홍')
# TypeError: greet() missing 1 required positional argument: 'msg'
greet('홍','안녕')

def greet(name, msg='안녕'):
    print(name+","+msg)

greet('홍') # 기본값으로
greet('홍','잘지내') # 지정값으로
# 만약 def greet(msg='안녕',name): 하게 되면
# default parameter는 앞으로 올 수 없는 syntax error 발생

# print('hi',end=' ') # end=' '이게 디폴트 매개변수임

# 3. 위치 매개변수(positional parameter)
# 매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장됨
# 매개변수의 순서대로 인수를 전달
# def add(a,b):
#     pass
# add(3,5)

# 4. 함수에 여러개 자료 전달 (리스트, 딕셔너리 등)
def show_names(names):
    for name in names:
        print(name,end=" ")
show_names(['홍길동','심청이','강감찬'])
print()
def show_info(info):
    print(info)
    for i,j in info.items():
        print(i,j)

infor={'이름':'홍길동','나이':20}
show_info(infor)

# 5. 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러 개의 값을 전달 받을 때 사용
# print(,,,,,) 처럼
# *args : tuple 형태로 데이터 전달  **kwargs=> key=value 묶어서 전달됨

# print('hi','hoho',end=' ')

# 1) *args 매개변수
def my_sum(*args):
    total=0
    for arg in args:
        total+=arg
    return total
print(my_sum(1,2))
print(my_sum(1))
print(my_sum(1,2,3))
print(my_sum(1,3,4,5))

# 2) **kwargs 매개변수

def show_info(**kwargs):
    for key in kwargs.keys():
        print(key, end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
    print()
    for item in kwargs.items():
        print(item)

show_info(id='abc')
show_info(id='abcd',name='hong')
show_info(id='abcd',name='hong',age=20)

# 6. 키워드 인수 (keyword arguments)
# 인수들 앞에 키워드를 두어서 인수를 구별
# 인수의 위치가 매개변수의 위치와 달라도 됨

def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40)

my_print(a=5,c=10,b=40)
my_print(5,c=10,b=40)
# my_print(c=10,30,2) # 뭐가 a,b인지 몰라


def show_info2(id, name, age):
    print(id)
    print(name)
    print(age)

show_info2('123','hong',20)
show_info2(id='123',age=30,name='hong')

# *args(위치인수)는 **kwargs(키워드 인수) 앞에 반드시 와야 함
def my_func(*args, **kwargs):
    pass

my_func(1,2,3, a=10, b=3)
# my_func(1, a=10,2,3,b=3) 안되죠. 위치 인수가 먼저 와야죠

# def my_func(*kwargs, *args):
# 이거는 안 됨. 키워드인수는 뒤에 와야 한다

def my_func(a,b,*args,c,d, **kwargs):
    pass
# a,b, *args 결국은 위치 인자라는거죠

# 함수호출:
# 위치인수와 키워드 인수 함께 사용하는 경우 키워드 인수가 위치인수 뒤로!
# 함수정의: 위치매개변수 뒤에 디폴트 매개변수 써야 함
