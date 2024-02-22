# 리스트 메소드 (함수)
# 1. append() : 리스트 맨 뒤에 항목을 추가

# a=[]
# a.append('apple')
# a.append('banana')
# a.append(19)
# print(f'alist:{a}')
#
# # 2. pop() : 리스트의 맨 마지막 요소를 추출하고 요소를 제거(꺼내다)
# # pop은 인덱스 지정 가능, 안 쓰면 디폴트 값은 index=-1
# value=a.pop()
# print(f'alist pop 적용: {a},value={value}')
# a.append('melon')
# print(f'alist {a}')
# print(f'alist : pop {a.pop(0)},pop 적용 후 {a}')
# # pop은 인덱스 지정 가능, 안 쓰면 디폴트 값은 index=-1
#
# # 3. sort() : 오름차순 정렬
# # 내림차순 위해서 reverse=True
# b=[6,3,5,1,-3]
# print(f'blist: {b}')
# b.sort()
# print(f'sort 적용 후: {b}')
#
# # 3.1 sort(key=str.lower)
# char=['b','B','A','a','z']
# print(f'charlist: {char}')
# # char.sort()
# # print(f'charList sort() 적용 후 : {char}')
# # char.sort(key=str.lower) # 대소문자 구분없이 정렬
# char.sort(key=str.lower,reverse=True)
# # ->zbBAa 내림차순
# print(f'charList sort(str) {char}')


# 4. reverse() : 리스트를 역순으로 변경

# print(f'blist reverse 적용 전: {b}')
# b.reverse()
# print(f'blist reverse 적용 후: {b}') #알파벳 내림차순

# 5. index() : 리스트에서 지정한 값의 위치를 반환
# 해당 값이 여러개더라도 제일 처음 찾은 인덱스 반환
#찾고자 하는 값이 없으면 ValueError 발생
# c=['홍길동','강감찬','성춘향','변학도','강감찬']
# idx=c.index('강감찬')
# print(f'clist index 적용:{idx}')
#
# # # 6. insert(위치,값) : 리스트에 값(요소) 삽입
# print(f'clist insert 전: {c}')
# c.insert(-1,"이몽룡")
# print(f'clist insert: {c}')

# 7. remove(값) : 리스트에서 지정한 값을 제거
# 값이 여러 개 존재할 때 remove는 첫번째 값만 지움
# 여러 개 지우고 싶으면 for 문 이용
# 8. count(값) : 리스트에서 지정한 값의 개수 반환
# print(f'clist: {c}')
# for item in range(c.count('강감찬')):
#     c.remove('강감찬')
#     #print(f'강감찬 삭제 {c}')
# print(f'clist remove : {c}')

# 9. extend() : 리스트에 리스트를 추가(확장)=>하나의 리스트로 변경
# b=[6,3,5,1,-3]
# print(f'blist {b}')
# b.extend([10,11,12]) # b+=[10,11,12]
# print(f'blist extend 후 :{b}')
# b.append([10,11,12])
# print(f'append 후: {b}')
# b.insert(3,[10,11,12])
# print(f'insert 후: {b}')

# b.extend(100)
# print(f'blist extend 후 :{b}')
# TypeError : extend는 리스트 형태!!
# 값 하나는 안 된다. int object is not iterable(list,tuple 등 여러 개 갖고 있는

# 10. sorted(reverse=False) : 오름차순, 내장함수, 리스트를 정렬한 새로운 리스트 반환
# sorted(d,reverse=True) 하면 내림차순
# 원본 유지
# d=['hotdog','melon','apple','kiwi']
# print(f'dlist {d}')
# new_d=sorted(d)
# print(f'sorted()함수 적용 후 dlist: {d}')
# print(f'dlist sorted:{new_d}')
# 원본 d는 적용 전과 같고, 새롭게 만들어진 리스트 출력하면 적용된 것 알 수 있죠.
# sort(), reverse()는 원본 변형

# 11. copy() : 리스트 복사
# a=[3,1,-10,11,2]
# cpy_a=a.copy()
# print(cpy_a)
# cpy_a.sort()
# print(cpy_a) #원본변형

# 12. clear() : 리스트를 비우기 (빈 리스트로)
# cpy_a.clear()   # cpy_a[:]=[] 동일한 기능
# print(cpy_a)
# cpy_a[:]=[]

# 13. del() : 리스트 요소 지우기, 리스트 전체 지우기
# 메모리 자체에서 지움
# del(cpy_a[3:])
# print(cpy_a)
# del(cpy_a) # 메모리에서 제거
# print(cpy_a) # NameError

# 14. len() : 리스트 길이
# print(len(a))

# 15. max() : 최대값을 반환하는 내장함수
# 16. min() : 최소값을 반환하는 내장함수

ex_list=[100,7,-2,99,30]

print(ex_list)
print(f'최대값 {max(ex_list)}')
print(f'최소값 {min(ex_list)}')
ex_list_str=['hello','Exit','Zoo','hI']
print(f'최대값 {max(ex_list_str)}')
print(f'최소값 {min(ex_list_str)}')

ex_lists=['hello','Exit','Zoo','hI','100','7']
print(f'최대값 {max(ex_lists)}')
print(f'최소값 {min(ex_lists)}')
# 100 7 Exit Zoo hI hello 순으로 최소->최대
# 즉 문자열로 된 숫자가 먼저 계산됨.
# 숫자와 문자가 같이 있으면 비교 연산 불가

ex_lists_h=['hello','Exit','홍길동' ,'춘향','방자',\
            'hI','100','7']
print(f'최대값 {max(ex_lists_h)}')
print(f'최소값 {min(ex_lists_h)}')
# 한글이 있을 경우 숫자-문자-한글 순으로 계산됨.

# 17. in, not in 연산자 : 리스트 내 원소 존재여부 True/False 반환

num=[1,2,3,4,5]
result=10 in num
print(result)
result=10 not in num
print(result)

# 18. > < >= <= == != : 리스트 일치 검사
# 리스트 길이, 요소 다 같아야 함
list1=[1,2,3]
list2=[1,3,2]
print(list1<list2)

