# 지역변수(local variable)와 전역변수(global variable)
# 지역변수 : 함수 내부에서 정의된 변수, 함수 안에서만 사용가능
#          함수 호출 시 생성되고, 함수종료되면 소멸되어 더 이상 사용 불가

a=10
# 전역변수이기 때문에 어디서든 사용 가능

def show_info(name):
    age=10
    print(name,age)
show_info('홍길동') #홍길동이 name에 전달
#print(name) #함수에서만 생존하는 지역변수!
# print(age) 함수 안에서만 사용되는 지역변수!
# 때문에 함수 밖에 영향을 주지 못한다

def show():
    a=1 # 지역변수
    a+=1
    print(f'a:{a}',id(a))

# 지역변수와 전역변수 이름이 같은 경우 지역변수가 우선한다
# 이름이 같더라도 공간이 다르잖아요


def show2():
    #a=a+1  # 지역변수를 찾음 : 오류발생
    # UnboundLocalError: cannot access local variable 'a'...
    b=a+1 # 전역변수 a 사용
    print(f'a:{a}', id(a))
    print(f'지역변수 b:{b}', id(b))


def show3():
    global a # 전역변수 사용
    a=a+1
    print(f'a:{a}', id(a))

print(f'전역변수 a: {a}',id(a))


def sub(x,y):
    global b
    a=7
    x,y=y,x
    b=3
    print(a,b,x,y)
a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y)
print(f'b는 {b}')

# 리스트, 딕셔너리 등의 경우 얕은 복사(위험)
def show_list(a):
    cpy_a=a.copy()
    cpy_a[-1]=100
    # a[-1]=100
    # print(a,id(a))
    print(cpy_a,id(cpy_a))
my_list=[1,2,3,4]
show_list(my_list)
print(my_list,id(my_list))









