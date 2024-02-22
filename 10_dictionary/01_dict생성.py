# 1. 딕셔너리 생성
# 집합적 자료, 순서 의미 없음
# key:value =>item
# {key1:value1, key2:value2, ...}
# {} or dict() 이용해 생성
# key로 데이터 접근

# d={}
d=dict()
print(d,type(d))

d2={1:'a',2:'b',3:'c'}
print(d2)
# key의 순서는 생성된 순서대로 구성
# key와 value는 사용자가 지정하는 것, 규정이 없다
# key는 숫자, 문자열 다 가능하나 유일하게 구별되어야 함
# value는 중복 가능

# 2. 딕셔너리 요소 접근 : key 사용
# 딕셔너리[키이름]

# 키로 접근하여 값을 가져옴
print(d2[1]) # 1은 인덱스가 아니라 키
# print(d2[0]) # KeyError: 0

# 3. 키를 이용하여 값 변경
d2[1]=10
print(d2)

# 4. 딕셔너리 요소 추가 : 딕셔너리[키]=값
d2[4]=100
print(d2)

# 5. 키는 유일한 값
# 동일한 키를 추가하는 경우 맨 마지막에 입력한 키가 적용
# {'a': 1, 'b': 1000, 'c': 'hello'}
d3={'a':1,'b':100,'c':'hello','b':1000}
print(d3)

# 6. value는 하나 또는 여러 개의 집합적 자료 가질 수 있음
d4={'name':['kim','hong','lee'],
    'score':[100,90,80],
    'gender':['F','M','M'],
    'phone':('123-234','123-909','010-1111')}
print(d4)
print(d4['name'])

# 7. 요소 삭제 : del(딕셔너리[키])
del(d4['gender'])
print(d4)






