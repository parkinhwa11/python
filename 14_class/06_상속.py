# 상속 : 부모클래스로부터 상속받은 필드와 메소드를 활이용하거나 추가 변경하여 활용 (재사용)
# 메서드 재정의 (overriding): 상속받은 메서드를 다시 정의
class Car(object):
    def __init__(self,speed=0,color=''):
        self.speed=speed
        self.color=color
    def drive(self):
        print(f'{self.speed}으로 주행한다')

class Truck(Car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color)
        self.load=load

    # 메소드 재정의 (overriding)
    def drive(self):
        print(f'{self.speed}으로 {self.load}톤의 짐을 싣고 주행한다')

    def loading(self):
        print(f'최대 {self.load}톤의 짐을 운반할 수 있는 트럭')

car1=Car(20,'blue')
truck1=Truck(30,'blue',5)
truck2=Truck(100,'white',10)
truck3=Truck(55,'black',7)
for car in [car1,truck1,truck2,truck3]:
    car.drive()
# 메소드 이름은 같지만 다른 기능을 수행한다.

# car1.drive()
# truck1.drive()
# truck1.loading()






