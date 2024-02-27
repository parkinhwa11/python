# 객체의 필요성

# 계산기 구현


class AddCal:

    def __init__(self):
        self.result=0
    def adder(self,num):
        self.result+=num
        return self.result

myadder=AddCal() #인스턴스 생성
myadder.adder(10)
myadder.adder(20)
myadder.adder(30)
print(myadder.result)

youradd=AddCal()
youradd.adder(23)
youradd.adder(20)
print(youradd.result)

print(type(myadder))
