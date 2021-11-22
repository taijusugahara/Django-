
from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()
from ModelApp.models import Person

# 全て取得
persons = Person.objects.all()
for person in persons:
    print(person.id,person,person.salary)

# person = Person.objects.get(first_name='Taro')
# person = Person.objects.get(first_name='taro')

person = Person.objects.get(pk=1) #主キー

print(person.id,person)

#filter(絞り込み、エラーにならない、複数取得)
print('*'*100)
persons = Person.objects.filter(first_name='Taro').all()
print(persons)

for person in persons:
    print(person.id,person)