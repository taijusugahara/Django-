# ジェネレータ関数
import sys


def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        yield n
        print('yield実行')


gen = generator(10)
# next()で実行
n = next(gen)
print(f'n={n}')
n = next(gen)
print(f'n={n}')

for x in gen:
    print(x)

# send:値を放出
# throw:例外を発生させる
# close:終了させる


def generator(max):
    print('ジェネレータ作成')
    for n in range(max):
        try:
            x = yield n  # ここが違う
            print(f'x = {x}')
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')


gen = generator(10)
next(gen)
gen.send(100)
gen.throw(ValueError('invald value'))
gen.close()
# next(gen)

# ジェネレーターの使い道はメモリ使用量を削減すること
# list,generator memory
list_a = [i for i in range(10000)]


def num(max):
    i = 0
    while i < max:
        yield i
        i += 1


gen = num(10000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(gen))

# サブジェネレータ


def sub_sub_generator():
    yield 'Sub Subのyield'
    return 'sub subのreturn'


def sub_generator():
    yield 'subのyield'
    res = yield from sub_sub_generator()  # returnで帰ってきた値をresに格納
    print(f'sub res = {res}')
    return 'subのreturn'


def generator():
    yield 'generatorのyield'
    res = yield from sub_generator()
    print(f'gen res = {res}')
    return 'generatorのreturn'


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
