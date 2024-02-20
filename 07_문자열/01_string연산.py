# 1. 문자열 생성

text='Python is programming language'

# 2. 문자열 인덱싱 : [인덱스]
# print('text[-1] :',text[-1])
# print('text[1] :',text[1])
# print('text[11] :',text[11])
#
# # 3. 문자열 슬라이싱 [start:end] [start:end:step]
# # 부분 문자열 반환
# print("text[2:10] :",text[2:10])
# print("text[2:10:2] :",text[2:10:2])
# print("text[::-1] :",text[::-1])
# print("text[1:14:-1] :",text[1:14:-1])
# print("text[::2] :",text[::2])
# print("text[:11] :",text[:11])
# print("text[2:] :",text[2:])
# print("text[11:2:-2] :",text[11:2:-2])

# 4. + 연산, * 연산, len()
name="kim"
age=20
hi='hello'
person=name+" "+str(age) #문자열과 숫자는 연결 불가하므로 str()로 형변환
print(person,type(person))

print(hi*5)

print("text의 길이는",len(text))

#5. 멤버연산 : in, not in
if'python'in text: #Python이면 존재
    print("exist")
else:
    print("not exist")

if'python' not in text:
    print("not exist")
else:
    print("exist")
# for의 in 연산에서 문자열 사용시 하나의 문자별로 작업
for ch in text:
    print(ch)

for i in text:
    print(i)





