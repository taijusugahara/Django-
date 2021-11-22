# クラスの継承

class Person:  # 親クラス
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'hello {self.name}')

    def say_age(self):
        print(f'{self.age} years old.')


class Employee(Person):  # Personの機能を継承
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def say_number(self):
        print(f'my number is {self.number}')

    def greeting(self):  # オーバーライド
        super().greeting()
        print(f'I\'m employee. 社員番号:{self.number} / {self.name}と申します')


man = Employee('田中', '30', 129)
man.say_number()
man.greeting()
man.say_age()
