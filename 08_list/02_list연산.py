# 1. 인덱싱(indexing) : 요소 접근

a=[1,2,3,4,5]
b=[[1,2],3,[5,6]]
print(a[0], a[-1], a[-3])
print(b[0],b[-1][0])

# 2. 슬라이싱(slicing) : 부분문자열

print('a[:]:', a[:])
print('a[1:]:', a[1:])
print('a[:2]:', a[:2])
print('a[::2]:', a[::2])
print('a[::-1]:', a[::-1])

# 리스트 값 변경 : 인덱스를 이용 a[i]=값, 값을 리스트로 주면 리스트로 바뀜

print('변경전 a list',a)
a[1]=100
print('변경후 a list',a)
a[2]=[10,20]
print('변경후 a list',a)

# 단, 슬라이싱으로 바꾸면 값만 바뀜
# [[30,40]]으로 하면 리스트로 들어감
a[1:2]=[30,40]
print('변경후 a list',a)

c=[10,20,30]
x,y,z=c
print(x,y,z)
# 10은 x에, 20은 y에, 30은 z에 할당

# 4. 리스트 합치기 : +
a=[1,2,3,4]
b=[7,8,[9,10]]
print('a+b:',a+b)

# 5. 리스트 곱하기(반복) : *
print('a*3:',a*3)

# 6. 리스트 복사 (copy) : 깊은 복사 vs. 얕은 복사
a=10
b=a
print('a=',a,'b=',b) # b 10
b=15
print('a=',a,'b=',b)
a=20
print('a=',a,'b=',b)
# a 값 변하지 않음, b만 변함!
# 직접형 자료들은 따로 놀아

a_list=[10,20,30,40]
b_list=a_list  # shallow copy(얕은 복사)
# 리스트는 복사되지 않고 주소값만 복사된 것임.

print('a_list',a_list,'b_list',b_list)
b_list[2]='apple'
print('a_list',a_list,'b_list',b_list)
print(id(a_list),id(b_list))

c_list=list(a_list) # deep copy(깊은 복사)
# 리스트의 복사본을 새로 생성하여 반환
print('a_list',a_list,'c_list',c_list)
a_list[0]='apple'
print('a_list',a_list,'c_list',c_list)
c_list[-1]='banana'
print('a_list',a_list,'c_list',c_list)
print(id(a_list),id(c_list))



# 인덱싱, 슬라이싱, +, *, 멤버 in not in, len()



