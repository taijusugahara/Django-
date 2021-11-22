num = 10
print(type(num))
num_str = str(num)
num_list =[num_str,'20','30']
num_list.append('40')
num_tuple = tuple(num_list)
# print(num_tuple)
num_tuple += input(), #タプルに追加 ,いる
print(num_tuple)
num_set ={'40','50','60'}
print(set(num_tuple) | num_set)
# num_dict = {key:value for key,value in zip(num_tuple,num_set)}
# print(num_dict)
num_dict ={
  num_tuple:num_str
}
print(num_dict)
print(len(num_list))

print(num_dict.get('Mykey','Does not exist')) #keyがなければ第二引数の処理

num_list.extend(['50','60']) #複数同時にリストに入れるときはextend
print(num_list)

val = input()
is_under_50 = int(val) <50
print(is_under_50)

print(f'num_str = {num_str}')

print(dir(num_dict)) #dirで関数一覧を表示