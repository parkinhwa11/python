# 튜플 생성
t=(1,)
print(t,type(t))
t=1,
# t=(1)
# print(t,type(t))

t1=(1,2,3)
print(t1,type(t1))

t2=4,5,6
print(t2)

t3=t1,(7,8,9)
print(t3)

t4=[1,2,3],[5,6,7]
print(t4)

# tuple(1,2,3)으로 쓰면 안 됨! []묶어서!!
t5=tuple([1,2,3])
print(t5)

t6=tuple('hello')
print(t6)

# 리스트를 튜플로 변환
list1=[1,2,3]
t7=tuple(list1)
print(list1,t7)

#튜플을 리스트로 변환
list2=list(t4)
print(t4,list2)

