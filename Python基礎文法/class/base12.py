# カプセル化 setter, getter その2

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):  # getter
        print('getter nameが呼ばれました')
        return self.__name

    @property
    def age(self):  # getter
        print('getter ageが呼ばれました')
        return self.__age

    @name.setter  # setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter  # setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age


human = Human('Koichi', 25)
print(human.name)
human.name = 'Makoto'
print(human.name)
human.age = -1
print(human.age)
