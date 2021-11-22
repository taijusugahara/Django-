from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()

from ModelApp.models import Students, Person

print('#'*100)
# print(Students.objects.all())

#IN
# ids = [13,14,15]
# print(Students.objects.filter(pk__in=ids))

#contain 部分一致
# print(Students.objects.filter(name__contains='三'))

#is null
# p = Person(
#   first_name='Jiro',last_name='Yamada',
#   birthday='2000-01-01',email='aa@aa.com',
#   salary=None, memo='memo jiro',web_site ='http://jiro.com'
# )
# p.save()
# print(Person.objects.filter(salary__isnull=True))
#exclude 指定した条件以外
# print(Person.objects.exclude(salary__isnull=True))
# print(Students.objects.exclude(name='太郎'))

#values 一部のカラムを取り出す
# print(Students.objects.values('name','age').filter(pk__gte=18))

# students = Students.objects.values('id','name','age')
# for student in students:
#   # print(student)
#   print(student['id'])

#order_by
# -降順
print(Students.objects.order_by('age'))
print(Students.objects.order_by('-name','id'))