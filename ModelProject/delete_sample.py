from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()
from ModelApp.models import Person

#一つ削除
# person = Person.objects.get(id=3)
# person.delete()

#複数削除
persons = Person.objects.filter(first_name='Taro').delete()

#全て削除
Person.objects.all().delete()
