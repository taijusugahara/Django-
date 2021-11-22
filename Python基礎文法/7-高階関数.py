# 高階関数
# 関数も変数として使用できる

# def print_hello():
#     print('hello')


# def print_goodbye():
#     print('good bye')


# var = ['A', 'B', print_hello, print_goodbye]
# print(var)
# var[2]()
# var[3]()

def print_world(msg):
    print(f'{msg} world')


def print_konnichiwa():
    print('こんにちは')


def print_hello(func):
    func('hello')  # ここでprint_world('hello)となる
    return print_konnichiwa


var = print_hello(print_world)
var()
