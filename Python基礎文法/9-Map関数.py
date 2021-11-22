# Map関数
# 同じ処理を複数の要素（リストや辞書）に使いたい時に使う

list_a = [1, 2, 3, 4, 5]
map_a = map(lambda x: x**2, list_a)
# print(list(map_a))
for x in map_a:
    print(x)

man = {
    'name': 'Ichiro',
    'age': '18',
    'country': 'Japan'
}
map_b = map(lambda x: x + ':' + man.get(x), man)
for x in map_b:
    print(x)


def calcurate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x-y


map_sample = map(calcurate, range(5), [3, 3, 3, 3, 3], [
                 'plus', 'minus', 'plus', 'minus', 'plus'])

for x in map_sample:
    print(x)
