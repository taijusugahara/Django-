import os
from django import setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam.settings')
setup()
from ModelApp.models import Students,Classes,Tests,TestResults

import random


class_list=['classA','classB','classC','classD','classE','classF','classG','classH','classI','classJ',]
student_list=['studentA','studentB','studentC','studentD','studentE','studentF','studentG','studentH','studentI','studentJ',]
test_list =['国語','数学','英語']


# for i in range(10):
#   print(random.randint(50,100))

# データ生成

# for test_name in test_list:
#     test = Tests(name=test_name)
#     test.save()

# for class_name in class_list:
#     cls = Classes(name=class_name)
#     cls.save()
#     for student_name in student_list:
#         student = Students(name=student_name, grade=1, class_name=cls)
#         student.save()
#         for test in Tests.objects.all():
#           test_result = TestResults(test=test, student = student, score = random.randint(50,100))
#           test_result.save()
        
# データ削除
# Tests.objects.all().delete()
# Students.objects.all().delete()

# データ読み込み

# id1番目のstudentのテストの成績
# student_1 = Students.objects.get(id=1)
# test_result_1 = TestResults.objects.filter(student_id=student_1)
# for test_result in test_result_1:
#   print(test_result.student.name, test_result.test.name,test_result.score)

#GROUP BY
from django.db.models import Max,Min,Avg,Sum
# print(Classes.objects.values('name').annotate(Sum('students.test_results.score'),Max('students.test_results.score'),Min('students.test_results.score'),Avg('students.test_results.score')))

test_results = TestResults.objects.values('test__name' ,'student__class_name__name').annotate(sum=Sum('score'),max=Max('score'),min=Min('score'),avg=Avg('score')).order_by('student__class_name')
for test_result in test_results:
  print(f"科目:{test_result['test__name']},クラス名：{test_result['student__class_name__name']}, 合計：{test_result['sum']}, 最大値:{test_result['max']},最小値:{test_result['min']},平均値:{test_result['avg']}")