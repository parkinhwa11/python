# students=[
#     {'name':'홍길동','korean':87,'math':98,'english':88,'science':95},
#     {'name':'이몽룡','korean':92,'math':98,'english':96,'science':98},
#     {'name':'성춘향','korean':76,'math':96,'english':94,'science':90},
#     {'name':'변학도','korean':98,'math':92,'english':96,'science':92},
#     {'name':'박지성','korean':95,'math':98,'english':98,'science':98},
#     {'name':'류현진','korean':64,'math':88,'english':92,'science':92}
# ]
#
# total=0
# print('이름\t총점\t평균')
# for student in students:
#     total=student['korean']+student['math']+student['english']+student['science']
#     avg=total/4
#     print(f'{student['name']}\t{total}\t{avg}')

dict={}
while True:
    word=input("영어 단어 등록 (종료는 quit) : ")

    if word in dict:
        print(f'{word}는 이미 등록된 단어 입니다.')
    else:
        mean = input(f'{word}의 뜻입력 (종료는 quit) : ')
        dict[word] = mean

    if word == 'quit' or mean == 'quit':
        break
print('\n')

while True:
    find=input("검색할 단어 입력 (종료는 quit) : ")
    if dict.get(find):
        print(f'{find}의 뜻은 {dict[find]}입니다')
    else:
        print(f'{find}는 사전에 없는 단어입니다.')
    if find=='quit':
        break








