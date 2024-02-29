## 함수
def addNumber(num):
    if num==1:
        return 1
    return num+addNumber(num-1)

## 메인
print(addNumber(100))

def factorial(num):
    if num<=1:
        print("1 반환")
        return 1
    print("%d*%d! 호출" %(num, num-1))
    retVal=factorial(num-1)

    print("%d*%d!(=%d)반환"%(num,num-1,retVal))
    return num*retVal
print('\n5!= ',factorial(5))