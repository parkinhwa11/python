# zip() 함수

foods=['떡볶이','짜장면','피자','라면']
sides=['김치','단무지','피클']

zip_list=list(zip(foods,sides))
zip_dic=dict(zip(foods,sides))
print(zip_list)
print(zip_dic)

# 리스트 컴프리헨션

xlist=[x*2 for x in range(1,11)]
print(xlist)

ylist=[x+y for x in range(1,11) for y in range(10,20)] #10*10=100 번 반복
print(ylist,'\n',len(ylist))

foodList=[(x,y) for x in ['밥','국수','짜장면'] for y in ['김치','콜라']]
print(foodList)

# 세트 컴프리헨션 : 중복 값 하나만
ySet={x+y for x in range(1,11) for y in range(10,20)}
print(ySet,'\n')

# 딕셔너리 컴프리헨션 : 키 값이 유일하므로 같은 키-다른 값->마지막 값만 남겠죠(피클)
print({food:side for food in foods for side in sides})

stds=['철수','영희','길동','순희']
std_dic={std:0 for std in stds}
print(std_dic)
print(std_dic.items())

stds={'철수':90,'영희':50,'길동':60, '순희':100}

stds_scores={name:'pass' if score>60 else 'non-pass'
             for name, score in stds.items() }
print(stds_scores)

# stds_scores2=dict()
# for name, score in stds.items():
#     if score > 60:
#         stds_scores2[name]='pass'
#     else:
#         stds_scores2[name]='non-pass'
# print(stds_scores2)

