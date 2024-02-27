# 재귀함수(recursive function)
# 함수 내부에서 자신의 함수를 다시 호출

# 1-n까지의 합 재귀함수
def my_sum(n):
    if n==1:
        return 1
    return n+my_sum(n-1)
print(my_sum(10))

# 1*2*...*n : n! 계산하는 재귀함수
# 반복문
def my_fact1(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(my_fact1(5))

# 재귀함수
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(5))


# 내부함수

def outFunc(x,y):
    def inFunc(a,b): # 밖에서 호출 불가
        return a+b
    return inFunc(x,y)
print(outFunc(10,30))

# 람다(lambda) 함수
# 한줄짜리 함수, return문 사용하지 않음
# 변수명 = lambda <인수들> : <반환할식>
# 람다함수는 함수 참조를 반환
# 변수로 람다함수 객체를 받아서 함수호출한다

f=lambda:1
print(f())

add=lambda x,y:x+y
print(add(2,3))

add=lambda x,y=30:x+y # 디폴트 매개변수
print(add(2))
print(add(10,50)) # y=50
print(add(y=100,x=10)) # 키워드 인수

# 람다 표현식 : 함수이름 명명하지 않고(변수에 할당하지 않고) 바로 호출
# (lambda 매개변수들:식) (인수들)

print((lambda x : x+10)(2))

#(lambda x : y=10; x+y)(10)
# syntax error 람다 함수 내에서 변수 생성 불가

y=10
print((lambda x:x+y)(10))
# 위의 경우처럼 전역변수 이용 or 두 변수 선언 or 디폴트 매개변수
print((lambda x,y:x+y)(10,10))
print((lambda x, y=10:x+y)(10))

def plus_ten(x):
    return x+10

(lambda x:x+10)

#[1,2,3,4,5]+10
new=[]
for i in [1,2,3,4,5]:
    new.append(i+10)
print(new)

# map과 함수 이용
print(list(map(plus_ten,[1,2,3,4,5])))

# map(함수이름, 데이터들)과 lambda 이용
print('lambda사용')
print(list(map(lambda x:x+10,[1,2,3,4,5])))
# 리스트 변환 안 하면 map 객체로 뜸

# 두 리스트 동일 인덱스 값 합
list1=[1,2,3,4]
list2=[10,20,30,40]
def addList(x,y):
    new=[]
    for i in range(len(x)):
        new.append(x[i]+y[i])
    return new
print(addList(list1,list2))

# map(function, iterable data) 함수
def add_two(x,y):
    return x+y
print(list(map(add_two,list1,list2)))

# lambda까지 이용해서 한 줄로
print(list(map(lambda n1, n2: n1+n2, list1,list2)))
