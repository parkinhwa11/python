# 함수 반환문 return

def get_area():
    w=int(input("가로길이: "))
    h=int(input("세로길이: "))
    return w*h

square=get_area()
print(f'넓이는 {square}이다')
# 만약 return문 없었으면 None 나옴

# 튜플 반환
def multi_return():
    return 1,2,3
# value=multi_return()
# print(value,type(value)) # type은 tuple
# a,b,c=multi_return() # 언패킹
# print(a,b,c, type(a)) # type은 int

# 리스트 반환
def get_names():
    names=[]
    for i in range(3):
        name=input("이름:")
        names.append(name)
    return names
n=get_names()
print(n)

# 딕셔너리 반환
def get_info():
    name=input('이름:')
    age=input('나이:')
    info={'name':name,'age':age}
    return info
information=get_info()
print(information)