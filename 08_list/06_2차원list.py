# 2차원 리스트 : [행][열]

# table=[[1,2,3,4],[7,8,9,10],[10,11,12,14]]
# print(table)
# print(len(table))
# print(table[0][1])
#
# for item in table:
#     print(item,type(item),len(item))
#
# for row in table:
#     for col in row:
#         print(col,end=" ")
#     print()
#--------------
# 행/열 동일하면 사용가능
# row_n=len(table)
# col_n=len(table[0])
#
# for r in range(row_n):
#     for c in range(col_n):
#         print(table[r][c],end=" ")
#     print()
#
# table2=[[1,2,3,4],[7,8,10],[10,11,12,14]]
# for row in table2:
#     for col in row:
#         print(col,end=" ")
#     print()

# 열 개수 일치하지 않으므로 오류남.
# row_n=len(table2)
# col_n=len(table2[0])
#
# for r in range(row_n):
#     for c in range(col_n):
#         print(table2[r][c],end=" ")
#     print()

# 4명의 국어, 영어, 수학 점수
# 2차원 리스트 이용해서 학생별 총점, 평균 구하기
# 내 방법
scores=[[90,85,70],[88,79,92],[100,100,100],[90,60,70]]
print('---성적표(점수)---')
for row in scores:
    print(row)
print('---성적표(점수,총점,평균)---')
for row in scores:
    total=sum(row)
    avg=total/3
    print(f'{row}, {total},{avg:.1f}')

# 다른 방법
print("--------")
std_scores=[[90,85,70],[88,79,92],[100,100,100],[90,60,70]]
print(std_scores)
print(len(std_scores))

for std in std_scores:
    print(std)

for std in std_scores:
    total=0
    for score in std:
        total+=score
    avg=total/len(std)
    print(f'{std},{total},{avg:.1f}')


