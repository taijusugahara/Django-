# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class_val'  # クラス変数

    def set_val(self):
        self.instance_val = 'instance_val'  # インスタンス変数 関数内で定義

    def print_val(self):
        print(f'クラス変数 = {self.class_val}')
        print(f'インスタンス変数 = {self.instance_val}')


instance_a = SampleA()  # インスタンス化
# instance_a.print_val()  # インスタンス変数をまだ作ってないのでそちらは表示されない
instance_a.set_val()
instance_a.print_val()

print(SampleA.class_val)  # クラス変数
print(instance_a.__class__.class_val)  # クラス変数

instance_b = SampleA()
instance_b.set_val()
instance_b.print_val()

instance_a.__class__.class_val = 'class val 2'  # クラス変数を変更
instance_b.print_val()
