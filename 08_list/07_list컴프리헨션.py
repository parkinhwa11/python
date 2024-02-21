# 리스트 컴프리헨션 (comprehension)
# 새로운리스트=[반복문장 for 변수 in 반복범위(range()) (if 조건식)]

# num_list=[]
# for num in range(1,6):
#     num_list.append(num)
# print(num_list)

# 리스트컴프리헨션으로
num_list=[num for num in range(1,6)]
print(num_list)

num_list2=[num*2 for num in range(1,6)]
print(num_list2)

num_list3=[num*num for num in range(1,6)]
print(num_list3)

# 1-20정수 중 짝수만으로 구성된 리스트 생성
even=[num for num in range(2,21,2)]
print(even)

even=[num for num in range(1,21) if num%2==0]
print(even)

# for num in range(1,21):
#     if num%2==0:
#         even.append(num)

# 문제. 1~20 정수 중 3의 배수 구성된 리스트
three=[num for num in range(3,21,3)]
print(three)

three=[num for num in range(1,21) if num%3==0]
print(three)

list1=[1,2,3,4,5]
num_list5=[num for num in list1 if num%3==0]
print(num_list5)

# 참고. zip : 쌍으로 묶고 맞지 않는 것은 버림.
# zip() : (떡볶이,단무지),(짜장면,김치),(라면,피클)
# 첫 쌍, 두 쌍, 세 쌍을 food와 side에 각각 할당
foods=['떡볶이','짜장면','라면','피자']
sides=['단무지','김치','피클']

#for food, side in zip(sides, foods,strict=True):
#이렇게 하면 오류남. foods,sides 순서 바꾸면

for food, side in zip(foods,sides):
    print(food,'--',side)

for item in zip(foods, sides):
    print(item)
print(type(zip(foods,sides)),zip(foods,sides))
print(list(zip(foods,sides)))

# name=['홍길동','강감찬','성춘향','방자']
# sex=['남','남','여','남']
# addr=['서울','한양','독도','부산']
# print(list(zip(name,sex,addr)))
#위의 한줄을 세줄로
# ob=zip(name,sex,addr)
#ob_list=list(ob)
#print(ob_list)



