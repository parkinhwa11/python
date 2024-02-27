# 예제. Dog 클래스

class Dog:
    dog_id=0 # 클래스 변수

    def __init__(self,name='',breed='',size='',age=0,Color=''):
        self.name=name
        self.breed=breed
        self.size=size
        self.age=age
        self.Color=Color
        Dog.dog_id=Dog.dog_id+1
    def eat(self,food):
        print(f'{self.name}가(이) {food}를 먹는다')
    def sleep(self):
        print(f'{self.name}가(이) 잠잔다')
    def sit(self):
        print(f'{self.name}가(이) 앉아있다')
    def run(self):
        print(f'{self.name}가(이) 뛴다')
    def __repr__(self):
        return f'{self.name}는(은) 품종:{self.breed}, 나이:{self.age}'

dog1=Dog("삐삐","Maltese","small",2,"white")
print(dog1.dog_id)

dog2=Dog("벤","Chow Chow","medium",3,"brown")
print(dog2.dog_id)
dog3=Dog("뭉치","Mastiff","large",5,"black")
print(dog3.dog_id)

dog1.eat("cheese")
dog1.sleep()
print(dog1)
print(dog2)

dog4=Dog()
print(f'dog4의 id {dog4.dog_id}')

# 인스턴스 변수 : 인스턴스가 소유하고 있는 변수
# 클래스 변수 : 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수
#   -> 클래스이름.클래스변수이름으로 메소드 내부에서 사용하고
#     외부에서는 인스턴스이름.클래스변수명으로 사용



