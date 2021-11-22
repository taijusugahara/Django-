# コンストラクタ デストラクタ

class SampleClass:
    def __init__(self, msg, name=None):  # コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg  # インスタンス変数
        self.name = name

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

    def __del__(self):
        print(f'{self.name}さん、デストラクタが実行されました')


var_1 = SampleClass('hello', 'jun')
var_1.print_msg()
var_1.print_name()

del var_1  # インスタンスを削除
