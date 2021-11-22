# ファイル入力

file_path = '../resources/input.csv'
f = open(file_path, mode='r', encoding='utf-8')
# line = f.read()  # 中身全体
# print(line)

# lines = f.readlines() #中身を配列で読み込む
# print(lines)
# for x in lines:
#     print(x.rstrip('\n'))

# line = f.readline() #1行ずつ読み込む
while (line := f.readline()):  # := セイウチ演算子
    print(line.rstrip('\n'))
    # line = f.readline()

f.close()

# with
with open(file_path, mode='r', encoding='utf-8') as f:
    while (line := f.readline()):
        print(line.rstrip('\n'))
