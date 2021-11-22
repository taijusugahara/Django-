from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()
from ModelApp.models import Person

from django.utils import timezone
import pytz

person = Person.objects.get(id=1)
print(person)
person.birthday = '2001-01-12'
person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
person.save()

# ＃一つ一つ複数更新
persons = Person.objects.filter(first_name='Taro').all()
for person in persons:
  person.first_name = person.first_name.lower()
  person.update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
  # person.save()

#一気に複数更新
Person.objects.filter(first_name = 'taro').update(
  web_site = 'https://taro.com',
  update_at = timezone.datetime.now(pytz.timezone('Asia/Tokyo'))
)