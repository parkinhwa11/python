# 함수
from random import randint, choice
def binSearch(ary,fdata):
    pos=-1 # 못찾았다 생각하고 찾으려고 노력해.

    start=0
    end=len(ary)-1
    while start<=end:
        mid=(start+end)//2
        if ary[mid]==fdata:
            pos=mid
            break
        elif ary[mid]<fdata:
            start=mid+1
        else:
            end=mid-1

    return pos # 못찾으면 -1 그대로 반환

# 변수
dataAry=[randint(30,190) for _ in range(10)] # 가족
findData=choice(dataAry) # 할머니키라 생각하면 됨, dataAry에서 임의로 하나 선택
dataAry.sort()

# 메인
print('배열-->',dataAry)
position=binSearch(dataAry,findData)
if position !=-1:
    print(findData,'는', position, '위치에 있어요')
else:
    print(findData, '는', position, '없어요ㅠㅠ')