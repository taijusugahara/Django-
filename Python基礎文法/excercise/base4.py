class CharacterAlreadyExistException(Exception):
    pass


class AllCharacters:
    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.alive_characters:
            raise CharacterAlreadyExistException('キャラクターは既に存在します')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)


class Character:
    def __init__(self, name, hp, offence, defence):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offence = offence
        self.defence = defence

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('キャラクターは既に死んでいます。')
            return

        if self.offence >= enemy.defence:
            enemy.hp -= (self.offence - enemy.defence)*critical_point
        else:
            enemy.hp -= 1 * critical_point

        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)

#####################


character_a = Character('AAA', 10, 5, 3)
character_b = Character('BBB', 8, 6, 2)
character_C = Character('CCC', 14, 1, 1)

print(character_b.hp)
character_a.attack(character_b)
print(character_b.hp)
character_a.critical_hit(character_b)
print(character_b.hp)

print(character_a.hp)
character_b.attack(character_a)
print(character_a.hp)

print(f'全キャラクター : {AllCharacters.all_characters}')
print(f'生き残っているキャラクター : {AllCharacters.alive_characters}')
print(f'死んでいるキャラクター : {AllCharacters.dead_characters}')
