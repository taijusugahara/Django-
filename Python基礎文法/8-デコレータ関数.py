# デコレータ関数

def my_decorater(func):
    def wrapper(*args, **kwargs):
        print('*'*100)
        # func
        func(*args, **kwargs)
        print('*'*100)
    return wrapper


@my_decorater
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)


@my_decorater
def func_b(*args, **kwargs):
    print('func_bを実行')
    print(args, kwargs)


func_a(1, 2, 3)
func_b(4, 5, 6, name='Taro')
