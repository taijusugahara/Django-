from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField()
    class_name = models.ForeignKey('Classes',on_delete=models.CASCADE)

    db_table = 'students'

class Classes(models.Model):
    name = models.CharField(max_length=50)

    db_table = 'classes'

class Tests(models.Model):
    name = models.CharField(max_length=50)

    db_table = 'tests'

class TestResults(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey('Students',on_delete=models.CASCADE)
    test = models.ForeignKey('Tests',on_delete=models.CASCADE)
    
    db_table = 'test_result'

