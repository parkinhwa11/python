# seek(offset,whence) 함수

print('파일 내에서 검색 : seek() ----')
f=open('data/seek_test_data.txt','r',encoding='utf-8')

f.seek(0,0)   # 시작위치:0, 0:파일처음
lines=f.readlines()
print(lines)

f.seek(3,0)
lines=f.readlines()
print(lines)


f.seek(8,0)
lines=f.readline()
print(lines)

f.seek(19,0) #  16가, 19나, 22다, 25라,utf-8의 경우, 한글은 세바이트씩 차지
lines=f.readlines()
print(lines)

f.close()