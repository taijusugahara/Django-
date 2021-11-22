# try except

try:
    b = [10, 20, 30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e:
    import traceback
    traceback.print_exc()  # 詳細を表示
    # print(e,type(e))
    pass  # 何もしなければpass

except IndexError as e:
    print('indexerror発生')

except Exception as e:
    print('Exception: ', e, type(e))

print('処理が完了しました')

# raise 例外を返す #例外自作


class MyException(Exception):
    pass


def devide(a, b):
    if b == 0:
        raise MyException('0では割り切れません')
    else:
        return a/b


try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))
