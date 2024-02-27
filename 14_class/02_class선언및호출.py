# 클래스 선언
# class 클래스 이름[(상속클래스)]:
#     클래스변수(필드) 선언
#     메서드 정의
#     def 메서드이름(self,매개변수들):
#          문장들

# 객체(인스턴스) 생성
# 이름=클래스명()  : 생성자

# 객체 : 단독으로 객체만 지칭
# 인스턴스(instance) : 클래스와 연관지어서 부를때

# 필드(변수)
# 메서드 정의
# self : 기존의 함수와 구분, 자신의 객체(인스턴스)임을 의미

# 예) 자동차 클래스 선언

class Car:
    color=''
    speed=0
    def drive(self):
        self.speed=10


# 인스턴스 생성
car1=Car()  # car() : 인스턴스 생성하는 생성자 함수
car2=Car()
car3=Car()

# 인스턴스의 필드 이용 : 인스턴스 이름.필드명
print(type(car1),id(car1))
print(type(car2),id(car2))
print(type(car3),id(car3))

# isinstance(인스턴스명, 클래스명) : 특정 클래스의 인스턴스인지 확인
print(isinstance(car1,Car))


# 인스턴스 생성 후 필드 추가하고 값 대입 가능
# car1.color='red'
# car2.color='green'
# car3.color='pink'
# car1.speed=0
# car2.speed=0
# car3.speed=0
# print(car1.color)

# 메서드 호출 :인스턴스 이름. 메서드명(인수들)
car1.drive()
print(car1.speed) # drive 호출하지 않았을 경우 단독으로 쓰면 오류남


print(f'car1의 speed {car1.speed}')
print(f'car2의 speed {car2.speed}')
print(f'car3의 speed {car3.speed}')





# 파이썬의 클래스들 : int, float, str, set, dict, list, tuple...
a=int(10)
print(a)
b=list(range(10))
print(b)
c=dict(x=10,y=20)
print(c)

print(type(a),type(b),type(c))
print(isinstance(a,int))
d=10.5
print(isinstance(d,float))
