# 다형성

class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')
class Cat(Animal):
    def talk(self):
        return 'Meow!'
class Dog(Animal):
    def talk(self):
        return 'woof woof!'
animals=[Cat('Missy'),Cat('Mr.Mistoffelees'),Dog('zion')]

for animal in animals:
    print(animal.name+': '+animal.talk())
