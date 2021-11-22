# ポリモーフォズム
# 同じメソッドだけどクラスによって違う処理になる
# 抽象メソッドにすることで必須としている

from abc import abstractclassmethod, ABCMeta


class Human(metaclass=ABCMeta):  # 親クラス
    # こうすることで抽象メソッドを呼び出せる
    def __init__(self, name):
        self.name = name

    @abstractclassmethod  # 抽象メソッド
    def say_something(self):  # 内容は書かない
        pass

    def say_name(self):
        print(self.name)


class Woman(Human):
    def say_something(self):
        print(f'女性: 名前は{self.name}')


class Man(Human):
    def say_something(self):
        print(f'男性: 名前は{self.name}')


# human = Woman('Hanako')

# ポリモーフィズム
num = input('0か1入力してください')
if num == '0':
    human = Man('Taro')
elif num == '1':
    human = Woman('Hanako')
else:
    print('入力が間違っています。')

human.say_something()
