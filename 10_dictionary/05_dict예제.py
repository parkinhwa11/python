# in / not in 연산자
# 딕셔너리에서는 키가 있는지 확인

d={'nine':9,'ten':10}

print('nine' in d) # key in dictionary

# 예제.
book={}
book['저자']='홍길동'
book['책제목']='파이썬'
book['출판일']='2020-01-30'
book['가격']=25000

# 북 딕셔너리의 키와 값을 모두 출력하시오.

for key in book.keys():
    # print('%s %s' % (key,book[key]))
    # print('{0}=>{1}'.format(key,book[key]))
    # print(key,'=>',book[key])
    print(f'{key} ==> {book[key]}')


# for key,value in book.items():
#     print(f'{key}, {value}')

