# ZeroDivisionError: division by zero

# print(10/0)


# TypeError
# print('나이는'+ 23 + '살')

# NameError
# print(b)

# ValueError: incomplete format
# c=100
# print('%d%'%c) %%로 해결

# SyntaxError
# if x>10
#     print('hello')

#IndexError: list index out of range
# a=[1,2,3,4]
# print(a[9])

# KeyError
# a={'0':0,'1':1,'2':2}
# print(a[3])

# UnboundLocalError
# def add():
#     a=a+1
# add()

#ModuleNotFoundError
# import mymodule

# FileNotFoundError
# with open('w.txt','r') as f:
#     f.read()

# OSError \f 가 escape 문자가 되기 때문에 argument 자체를 잘못 줬다
# with open('c:\file\data\w.txt', 'r') as f:
#     f.read() \보다 /를 쓰던가 \\두번 쓰던가

try:
    for i in range(1,7):
        result=7//i
        print(result)
except ZeroDivisionError:
    print("Not divided by 0")
finally:
    print("종료되었습니다")







