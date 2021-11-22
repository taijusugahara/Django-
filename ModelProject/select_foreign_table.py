from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()
from ModelApp.models import Students,Schools,Prefectures

s = Schools.objects.first()
print(type(s))
print(dir(s))
print(s.prefecture.name)
print(s.students_set.all())


#1対1
from ModelApp.models import Places,Restaurants

p = Places.objects.first()
print(type(p))
print(dir(p))
print(p.restaurants.name)
r= Restaurants.objects.first()
print(r.place.name)


#多対多
from ModelApp.models import Books,Authors

b = Books.objects.first()
print(b.authors.all())
r = Authors.objects.first()
print(r.books_set.all())