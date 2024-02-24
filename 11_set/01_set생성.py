# 세트

# 1. 순서가 없다 : 입력되는 순서와 출력되는 순서는 다를 수 있다
# 2. 동일한 요소(값)는 중복될 수 없다
# 3. 인덱스 사용 불가
# 4. 요소 추가/삭제 가능
# 5. 변경 가능한 항목을 세트의 요소로 가질 수 없다. unhashable type 안 됨
#    - 리스트를 세트의 요소로 가질 수 없다
#    - 튜플은 포함할 수 있다

# 키만 모아놓은 딕셔너리의 특수한 형태
# 세트(집합) 생성 : {}, set()

# 세트 생성
s1={1,2,3,4,5,1,2,3}
print(s1,type(s1))

s2=set([10,8,11,20,30,10])
print(s2)

s3=set((100,200,300,200,150))
print(s3)

s4=set({'one':1,'two':2}) # 키 값만 셋으로
print(s4)

# print(s1[0]) 인덱스 불가
# TypeError: 'set' object is not subscriptable

# 리스트는 세트 요소로 불가
# s5={1,2,[4,3]}
# print(s5)
# TypeError: unhashable type: 'list'

s5={1,2,(4,5)}
print(s5) # 튜플은 요소로 가능

# hashable type => hashing
# 객체를 식별할 수 있는 코드를 부여하여 테이블에 저장하는 방식 : (키, 값)


