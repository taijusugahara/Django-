# インスタンスメソッド ・クラスメソッド ・スタティックメソッド
# クラスメソッドはインスタンス化せずに使用できる
# スタティックメソッドはただの関数。インスタンスやクラスが引数に渡されることはない

class Human:
    class_name = 'Human'  # クラス変数

    def __init__(self, name, age):  # コンストラクタ
        self.name = name
        self.age = age

    def print_name_age(self):  # インスタンスメソッド
        print('インスタンスメソッド実行')
        print(f'name = {self.name}, age = {self.age}')

    @classmethod
    def print_class_name(cls, msg):  # クラスメソッド cls必須
        print('クラスメソッド実行')
        print(cls.class_name)  # クラス変数
        print(msg)

    @staticmethod
    def print_msg(msg):  # スタティックメソッド
        print('スタティックメソッド実行')
        print(msg)


Human.print_class_name('こんにちは〜〜〜')
man = Human('雷火', 22)
man.print_name_age()
# スタティックメソッド
man.print_msg('hello static')
Human.print_msg('hello')
