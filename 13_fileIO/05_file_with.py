# with문 : close()가 자동으로 수행
# with open(파일명,모드) as 파일객체:
#    수행문장들

# with open('study_data2.txt','r') as f:
#     text=f.read()
#     print(text)
#
# with open('data/file1.txt','a',encoding='utf-8') as f2:
#     f2.write(text)

# scores.txt:탭으로 구분한 데이터 파일
with open('data/scores.txt','r',encoding='utf-8') as f3:
    data=f3.readlines()
    print(data)

# scores2.txt:,으로 구분한 데이터 파일
with open('data/scores2.txt','r',encoding='utf-8') as f4:
    data=f4.readlines()
    print(data)

print(len(data))

score=[]
for i in range(len(data)):
    temp=data[i]
    temp=temp.rstrip('\n')
    score=score+temp.split(',')

print('score',score)


