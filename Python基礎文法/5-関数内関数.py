# inner関数 ノンローカル関数

def outer():
    outer_value = '外側の変数'

    def inner():
        # 内側の変数を外側でも使える。更新できるようにする
        nonlocal outer_value
        outer_value = '内側の変数'
        print(f'inner_value = {outer_value}')
        print('A')
    inner()
    print(f'outer_value = {outer_value}')


outer()
