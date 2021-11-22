from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
# 環境変数          #setting.pyがある場所
setup()

from ModelApp.models import Students

#件数 count
# print(Students.objects.count())
# print(Students.objects.filter(name='太郎').count())

#件数、最大値、最小値、平均値、合計
from django.db.models import Count,Max,Min,Avg,Sum
# print(Students.objects.aggregate(Count('pk'),Max('pk'),Min('pk'),Avg('pk'),Sum('age')))
# aggregate_student = Students.objects.aggregate(Count('pk'),Max('pk'),Min('pk'),Avg('pk'),Sum('age'))
# print(aggregate_student['pk__max'])
#名前を付けれる max=Max//とするだけ maxが名前
# aggregate_student = Students.objects.aggregate(count=Count('pk'),max=Max('pk'),min=Min('pk'),avg=Avg('pk'),sum=Sum('age'))
# print(aggregate_student)

#GROUP BY
print(Students.objects.values('name').annotate(
  max=Max('pk'),min=Min('pk')
))
print(Students.objects.values('name').annotate(
  max=Max('pk'),min=Min('pk')
).query)

print(Students.objects.values('name','age').annotate(
  max=Max('pk'),min=Min('pk')
))

students = Students.objects.values('name','age').annotate(
  max=Max('pk'),min=Min('pk')
)
for student in students:
  print(student['name'],student['max'])