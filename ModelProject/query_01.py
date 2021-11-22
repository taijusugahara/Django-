from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()

from ModelApp.models import Students

#全権取得
# print(Students.objects.all())

#頭5件取得
# print(Students.objects.all()[:5])

#5件目より後ろ
# print(Students.objects.all()[5:])

#5~7
# print(Students.objects.all()[5:8])

###どういったsqlが実行されているのか query
# print(Students.objects.all()[5:8].query)

#1番最初の一件
# print(Students.objects.first())

#同じもののみ
# print(Students.objects.filter(name='太郎'))
# print(Students.objects.filter(age=17))

#AND条件
# print(Students.objects.filter(name='太郎', pk__gt=15)) 
# print(Students.objects.filter(name='太郎', pk__gt=15).query) 
# gt = greater than, lt = less than

#前方一致、後方一致
# print(Students.objects.all())
# print(Students.objects.filter(name__startswith='太'))
# print(Students.objects.filter(name__endswith='郎'))

#or
from django.db.models import Q
print(Students.objects.filter(Q(name='太郎') | Q(pk__gt=19)))
print(Students.objects.filter(Q(name='太郎') | Q(pk__gt=19)).query)