# 내장 함수들

# abs() : 절대값
print(abs(-10))

# all(iterable) : 모두 True인 경우 True
# any(iterable) : 하나라도 True인 경우 True
print(all([0,1,2]))
print(any([1,0,[],""]))

# chr(i) : 아스키 코드값에 해당하는 문자 반환
print(chr(97))
# ord(c) 문자에 해당하는 아스키 코드값 반환
print(ord('a'))

# divmod(), pow()
# min(), max(), sum()
print(max([1,2,3,4,-10]))

# round(number, ndigits) : 실수 소수점 이하 자리수까지 반올림하여 반환
print(round(3.141592,2))
print(round(3.541592)) # 소수점 이하 자리수 지정 안 하면 첫째 자리 반올림 적용 후 정수부분만 출력

# enumerate(iterable, start=0) : 인덱스값을 포함한 enumerate 객체 반환
data=['kim','lee','choi']
print(list(enumerate(data)))

for item in enumerate(data):
    print(item)

for idx,value in enumerate(data):
    print(idx, value)
    print(data[idx])

for idx, value in enumerate("Hello world!"):
    print(idx,value)

# eval(expression) : 표현식의 연산 결과 반환
print(eval('1')+eval('2'))
print(eval('1+3'))

# filter(function, iterable) : 반복가능한 자료에 어떤 함수를 적용하여 True인 결과만 추출
def positive(x):
    return x>0
print(positive(10))
print(positive(-10))

print(list(map(positive,[1,2,-1,10,-5])))
# True, False 로만 나오는 함수를 filter를 통해 값으로 출력!
print(list(filter(positive,[-1,0,40,5])))

def even(x):
    if x%2==0:
        return x
print(list(filter(even,[-1,0,40,5])))

# help() : 도움말 시스템 호출
# help(print)
# help(filter)
# help(sum)

# int(), float(), str()
# input(), print()
# hex(), bin(), oct()
# list(), tuple(), dict(), set()
# range(), len()
# zip(), map()
# id(), type()
# sorted()
# lambda


