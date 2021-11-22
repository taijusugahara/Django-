# メタクラス クラスの再定義
# この次の抽象メソッドを使うのに必要

class MetaException(Exception):
    pass


class Meta1(type):  # type(デフォルトのメタクラス)
  # def __new__とreturn super().__new__が必要
    def __new__(metacls, name, bases, class_dict):
        print(f'metacls = {metacls}')
        print(f'name = {name}')
        print(f'bases = {bases}')
        print(f'class_dict = {class_dict}')
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください。')
        for base in bases:  # 継承しているクラス
            if isinstance(base, Meta1):
                raise MetaException('継承できません。')
        return super().__new__(metacls, name, bases, class_dict)


class ClassA(metaclass=Meta1):
    a = '123'
    my_var = 'AAA'
    pass


class SubClassA(ClassA):
    pass
