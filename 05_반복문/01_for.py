# for x in range(3):
#     for y in range(1,5):
#         print(y+4*x, end=" ")
#     print()
# a=1
# for x in range(3):
#     for y in range(4):
#         print(a, end=' ')
#         a+=1
#     print()

#구구단
for dan in range(10):
    for i in range(10):
        print(f'{dan:2d}*{i:2d}={dan*i:>2}')
    print()