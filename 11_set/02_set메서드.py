# set 메서드

s={10,1,3,4}
print(s)

# 1. 데이터 추가
# add() 메서드 : 집합에 요소 추가
s.add(100)
print(s)

# update() 메서드
s.update([5,6])
print(s)

# 2. 데이터 삭제, 추출
# pop() : 맨 앞 요소 가져오네?
result=s.pop()
print(result)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

s.update([10,11,12,13,14])
print(s)

# remove(값)
s.remove(10)
print(s)
# s.remove(15) # 삭제하려는 값이 없으면 KeyError

# discard(값)
s.discard(6)
print(s)
s.discard(7) # print 하면 None 출력
print(s) # 삭제하려는 값이 없으면 아무 변화없음

# clear()
s.clear()
print(s)

# 연산
s1={1,2,3}
s2={3,4,5}
# 합집합 : union(), |(or)
print(s1.union(s2)) # 또 다른 셋
print(s1|s2)

# 교집합 : intersection(), &(and)
print(s1.intersection(s2))
print(s1&s2)

# 차집합 : difference(), -
print(s1.difference(s2)) # s1에만 있는 것
print(s2.difference(s1)) # s2에만 있는 것
print(s1-s2)
print(s2-s1)











