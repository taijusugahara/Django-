# private変数
# __でprivate変数 クラス外からアクセスできないもの
# クラス内からはアクセスできる

class Human:
    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name  # private変数
        self.__age = age

    def print_msg(self):
        print(f'name ={self.__name}, age={self.__age}')


human = Human('Taro', 15)
# print(human.__name)  # アクセスできない
human.print_msg()
