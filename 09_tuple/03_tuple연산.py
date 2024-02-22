# 복수개 자료 치환

a,b=1,2
print(a, b, type(a), type(b))

a,b=b,a
print(a, b)

(a,b),(c,d)=(10,11),(12,13)
print(a,b,c,d)

# 패킹(packing)
t=1,2,'hello'
print(t)

# 언패킹(unpacking)
x,y,z=t
print(type(t))
print(x,y,z,type(x),type(y),type(z))

# * : 값을 여러 개 갖고 있는 변수구나. 대표적으로 list
# a는 하나의 값만 대응, 나머지는 묶어서 b에 대응. list 형태로!
# 이것 또한 언패킹
t2=(1,2,3,4,5)
a,*b=t2
print(a,b,type(a),type(b))
a,b,*c=t2
print(a,b,c)
*a,b,c=t2
print(a,b,c)

# *a,*b,c=t2
# print(a,b,c) 몇 대 몇으로 나눠가질지 모르죠
# SyntaxError: multiple starred expressions in assignment

