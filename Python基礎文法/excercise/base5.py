from abc import abstractclassmethod, ABCMeta


class Animals(metaclass=ABCMeta):
    @abstractclassmethod
    def speak(self):
        pass


class Dog(Animals):
    def speak(self):
        print('わん')


class Cat(Animals):
    def speak(self):
        print('にゃー')


class Sheep(Animals):
    def speak(self):
        print('めー')


class Other(Animals):
    def speak(self):
        print('そんな動物いません')


animal_num = input("1:dog,2:cat,3:sheep,その他:other > ")
if animal_num == '1':
    animal = Dog()
elif animal_num == '2':
    animal = Cat()
elif animal_num == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak()
