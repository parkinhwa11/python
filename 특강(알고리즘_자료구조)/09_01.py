# 함수
from random import randint, choice
def seqSearch(ary,fdata):
    pos=-1 # 못찾았다 생각하고 찾으려고 노력해.
    for i in range(len(ary)):
        if ary[i]==fdata:
            pos=i # 찾았으면 해당 인덱스값 반환
            break
    return pos # 못찾으면 -1 그대로 반환


# 변수
dataAry=[randint(30,190) for _ in range(8)] # 가족
findData=choice(dataAry) # 누나키라 생각하면 됨, dataAry에서 임의로 하나 선택
print(findData)
# 메인
print('배열-->',dataAry)
position=seqSearch(dataAry,findData)
if position !=-1:
    print(findData,'는', position, '위치에 있어요')
else:
    print(findData, '는', position, '없어요ㅠㅠ')