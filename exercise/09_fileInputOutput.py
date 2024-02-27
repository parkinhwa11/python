#1번
# with open("../13_fileIO/data/s.txt", 'r') as f1:
#     data=f1.readlines()
#     print(data)
#
# sorted_data=sorted(data)
# print(sorted_data)
# for line in sorted_data:
#     print(line.strip())

# 2번
# path='../13_fileIO/data/yesterday.txt'
# with open(path,'r') as f:
#     data=f.read()
#     data_lower=data.lower()
#     print(data_lower)




# 3번

# def my_sum(inputfile,outputfile):
#     with open(inputfile,'r') as f1:
#         data=f1.readlines()
#     with open(outputfile,'w') as f2:
#         for line in data:
#             numbers=line.strip().split()
#             a=list(map(int,numbers))
#
#             if a!=[]:
#                 total=sum(a)
#                 f2.write(f'{a[0]}+{a[1]}={total:.1f}')
#
#
# my_sum("../13_fileIO/data/a.txt","../13_fileIO/data/b.txt")

# 4번

def input_member(inputfile):
    while True:
        mem=input("멤버를 입력하세요. (종료는 q) : ")
        if mem=='q':
            break
        with open(inputfile,'a',encoding='utf-8') as f1:
            f1.write(mem+'\n')
def output_member(outputfile):
        with open(outputfile,'r',encoding='utf-8') as f2:
            print(f2.read())
while True:
    choice = input("저장 1, 출력 2, 종료 q : ")
    if choice=='1':
        file_name=input("멤버 명단을 저장할 파일명을 입력하세요. :")
        input_member(file_name)
    elif choice=='2':
        savedFile=input("멤버 명단이 저장된 파일명을 입력하세요. : ")
        output_member(savedFile)
    elif choice=='q':
        break
    else:
        print("올바른 선택을 입력하세요.")





