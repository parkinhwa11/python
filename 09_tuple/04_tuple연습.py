# 2차원 튜플 생성

t=((1,2,3),(4,5,6),(7,8,9))
print(t)

# 2차원 튜플의 요소를 행렬의 테이블 형식으로 출력
for i in t:
    print(i)

# 방법 1
for i in t:
    for j in i:
        print(j,end=" ")
    print()

# 방법 2
for r in range(len(t)):
    for c in range(len(t[r])):
        print(t[r][c],end=' ')
    print()

# 방법 3 언패킹
for i in range(len(t)):
    lt1,lt2,lt3=t[i]
    print(lt1,lt2,lt3)


