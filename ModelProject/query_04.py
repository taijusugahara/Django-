from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()

from ModelApp.models import Students

print('*'*100)

# for student in Students.objects.all():
#   print(student.name,student.school.name,student.school.prefecture.name)

#外部テーブルーでフィルター
# for student in Students.objects.filter(school__name='南高校'):
#     print(student.name,student.school.name,student.school.prefecture.name)

#外部テーブルでexclude
# for student in Students.objects.exclude(school__name='南高校'):
#     print(student.name,student.school.name,student.school.prefecture.name)

#ORDER BY
# for student in Students.objects.order_by('school__name'):
#     print(student.name,student.school.name,student.school.prefecture.name)

#GROUP BY
from django.db.models import Count,Max,Min,Avg,Sum
print(Students.objects.values('school__name').annotate(Count('pk'),Max('pk'),Min('pk'),Avg('pk'),Sum('pk')))