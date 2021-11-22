# カプセル化 getter, setter その1
#次のやり方の方がよく使うらしい

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter name を呼び出しました')
        return self.__name

    def get_age(self):
        print('getter age を呼び出しました')
        return self.__age

    def set_name(self, name):
        print('setter name を呼び出しました')
        self.__name = name

    def set_age(self, age):
        print('setter age を呼び出しました')
        self.__age = age

    # プロパティが必要
    # nameを指定するとgetter_name,setter_nameが呼び出される
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)


human = Human('Taro', 15)
human.name = 'Jiro'
human.age = 18
print(human.name)
print(human.age)
human.print_msg()
