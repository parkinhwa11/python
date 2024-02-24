# 1. get() 메서드

d={'one':1,'two':2,'three':3}
print(f'd["two"] : {d['two']}')

print(f'd.get("two") : {d.get('two')}')

# print(d['four']) # KeyError: 'four'
print(f'd.get("four") : {d.get('four')}') # 키가 존재하지 않는 경우 None 반환
print(d.get('four',4)) # key가 없는 경우 두번째 인수 반환
print(d)

# 2. setdefault() 메서드
print(d)

print(d.setdefault('two')) # 해당 value 반환
print(d.setdefault('two',20)) # 그래도 2 반환
d.setdefault('four',4)
print(d)

# 3. pop(), popitem() 메서드
print(d.popitem()) # 제일 뒤의 요소(키,값)을 튜플로 가져옴
key,value=d.popitem() # 제일 뒤 요소 또 변경되겠죠
print(f'key={key}, value={value}')
print(d)

d['six']=6
d['ten']=10
print(d)

result=d.pop('two') #인수(argument) 필요
print(result)
print(d)
#d.pop('seven')
#print(d) #KeyError: 'seven'

# 4. copy()
d2=d.copy()
print(d,id(d))
print(d2,id(d2))
d2['four']=4
print(d)
print(d2)

# 5. update() 리스트의 extend() += 처럼
d.update(d2)
print(d) # 공통요소 빼고 d2에만 있는 요소만 추가됨

d3={'five':5,'two':'2','seven':7}
print(d3)
d3.update(d2)
print(d3) # d3에 d2 추가해서 하나의 딕셔너리로

# 6. clear()
print(d,id(d))
d.clear()
print(d,id(d)) # 메모리 동일

print(d2,id(d2))
d2={} # 새로운 딕셔너리 생성
print(d2,id(d2)) # 다른 메모리 가리킴


