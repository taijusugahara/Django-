from django.utils import timezone
from django.db import models
# import pytz


# Create your models here.


class BaseMeta(models.Model):
    create_at = models.DateTimeField(
        default=timezone.datetime.now)
    update_at = models.DateTimeField(
        default=timezone.datetime.now)

    class Meta:
        abstract = True


class Person(BaseMeta):
    # indexは検索に用いるものだけに使用する
    # null falseはデフォルト値なんだ
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1900-01-01')
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    web_site = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'person'
        index_together = [['first_name', 'last_name']]
        ordering = ['-salary']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Students(models.Model):
    name = models.CharField(max_length=20)
    age= models.IntegerField()
    major = models.CharField(max_length=20)
    school = models.ForeignKey(
        'Schools', on_delete=models.RESTRICT
    )
    prefecture = models.ForeignKey(
        'Prefectures',
         on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.pk},{self.name},{self.age}'


    class Meta:
        db_table = 'students'


class Schools(models.Model):
    name = models.CharField(max_length=20)
    prefecture = models.ForeignKey(
        'Prefectures', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'schools'


class Prefectures(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'prefectures'

######################################
# 1対1

class Places(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        db_table = 'places'


class Restaurants(models.Model):
    place = models.OneToOneField(   #1対1の紐付け
        Places,
        on_delete=models.CASCADE,
        primary_key=True
    )
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'restaurants'

#####################################
# 多対多

class Authors(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'


class Books(models.Model):
    name = models.CharField(max_length=50)
    authors = models.ManyToManyField(Authors)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'books'