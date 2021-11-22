# ファイル出力、追記

file_path = '../resources/output.csv'

f = open(file_path, mode="w", encoding='utf-8', newline='\n')
f.write('あああ\nいいい')

with open(file_path, mode="a", encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['1', '2', '3']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))
    # f.writelines(list_a[0])


with open(file_path, mode="r", encoding='utf-8') as f:
    while (line := f.readline()):
        print(line.rstrip('\n'))
