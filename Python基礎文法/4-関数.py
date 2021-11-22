# デフォルト値、可変長引数、複数の返り値

def sample(arg1, arg2=100):
    print(arg1, arg2)


sample(200)


def spam(arg1, *arg2):
    print(f'arg1 = {arg1}, arg2 = {arg2} ')
    print(type(arg2))


spam(1, 2, 3, 4, 5)


def spam_2(arg1, **arg2):
    print(f'arg1 = {arg1}, arg2={arg2}')
    print(type(arg2))


spam_2(3, name='Taro', age=20)

# 複数の返り値


def sample_2():
    return 1, 2


a, b = sample_2()
print(a)
