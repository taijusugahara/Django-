from django.db import models
from django.contrib.auth.models import(
  BaseUserManager,AbstractBaseUser,PermissionsMixin
)


class UserManager(BaseUserManager):

  def create_user(self,username,password,email=None):
    if not email:
      raise ValueError('Enter Email!')
    user = self.model(
      username=username,
      email = email
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,username,email,password=None):
    user = self.model(
      username=username,
      email = email
    )
    user.set_password(password)
    user.is_staff = True
    user.is_active = True
    user.is_superuser = True
    user.save(using=self._db)
    return user



class User(AbstractBaseUser,PermissionsMixin):
  username = models.CharField(max_length=150)
  email = models.EmailField(max_length=255, unique=True)
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  website = models.URLField(null=True)
  picture = models.FileField(null=True)
  #パスワードは既にあるので書く必要なし

  USERNAME_FIELD = 'email' #このテーブルのレコードを一意に識別
  REQUIRED_FIELDS = ['username'] #スーパーユーザー作成時に入力する

  objects = UserManager()

  def __str__(self):
    return self.email


class Students(models.Model):

  name = models.CharField(max_length=20)
  age = models.IntegerField()
  score = models.IntegerField()
  school = models.ForeignKey(
    'Schools', on_delete=models.CASCADE
  )

  def __str__(self): #管理画面でobjectで表示されるところを
    return self.name + ': ' + str(self.age)

  class Meta:
    db_table = 'students'
    verbose_name_plural = '生徒'
    ordering = ('-score',)

class Schools(models.Model):
  name = models.CharField(max_length=20,verbose_name='学校名')

  def __str__(self): #管理画面でobjectで表示されるところを
    return self.name

  class Meta:
    db_table = 'schools'
    verbose_name_plural = '学校'

