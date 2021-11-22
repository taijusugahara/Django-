from random import randint


def generate_enemy_choices():
    while True:
        yield '1'
        yield '2'
        yield '3'


choices = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

lose_count = 0
enemy_choices = generate_enemy_choices()


def lose_func():
    global lose_count
    if lose_count == 3:
        print('あなたの負けです')
        return 'over'
    else:
        print("あなたの負け、再チャレンジ")


while True:
    my_choice = input("1,2,3から一つ選択してください(1:グー,2:チョキ,3:パー) : ")
    if my_choice not in ('1', '2', '3'):
        print('間違った入力です')
        continue
    enemy_choice = next(enemy_choices)
    # enemy_choice = str(randint(1, 3))  # ランダムにしたければ
    print(
        f"あなたの出した手：{choices.get(my_choice)}、相手の出した手：{choices.get(enemy_choice)}")

    if my_choice == "1":
        if enemy_choice == "2":
            print("あなたは勝ちました")
            break
        elif enemy_choice == "3":
            lose_count += 1
            if lose_func() == 'over':
                break
        else:
            print("あいこ")

    elif my_choice == "2":
        if enemy_choice == "3":
            print("あなたは勝ちました")
            break
        elif enemy_choice == "1":
            lose_count += 1
            if lose_func() == 'over':
                break
        else:
            print("あいこ")

    elif my_choice == "3":
        if enemy_choice == "1":
            print("あなたは勝ちました")
            break
        elif enemy_choice == "2":
            lose_count += 1
            if lose_func() == 'over':
                break
        else:
            print("あいこ")
