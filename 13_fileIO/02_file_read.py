# 텍스트파일을 읽기

# 텍스트파일 생성 : 메모장을 이용해서
# study_data.txt : 한글 -> 오류 발생
# study_data2.txt : 영문

f=open('data/study_data.txt', mode='r', encoding='utf-8')
# # UnicodeDecodeError : 'cp949' codec can't decode...
# # utf-8 모드인데 cp949로 달라서 encoding='utf-8' 추가!
# t=f.read()
# print(t)
# f.close()
#
# # 1단계 : 파일열기(open) # 'r', 'read'
# f1=open('study_data2.txt', mode='r')
#
# # 2단계 : 파일처리(읽기)
# t2=f1.read()
#
# print(t2)
# #3단계 : 파일닫기 (close())
# f1.close()

# ANSI 로 했을 경우, encoding 안 해도 됨
# f2=open('study_data3.txt', mode='r')
# t3=f2.read()
# print(t3)
# f2.close()

# readline()
# t1=f1.readline()
# print(t1)
# t11=f1.readline()
# print(t11)

# while True:
#     text=f.readline()
#     if not text: # 읽을 내용이 없으면(마지막)
#         break
#     print(text)

# readlines() : 리스트형태
# texts=f.readlines()
# print(texts)

# 1) 파일객체.readlines()
# for textline in f.readlines():
#     # print(textline,end='') # 줄바꿈 안 됨.
#     print(textline.strip())
# f.readline()과 같은 결과

# 2) readlines() 없이 파일객체 바로 써도 됨.
for textline in f:
    print(textline)

f.close()

# seek() : 내가 탐색하고자 하는 위치 지정

