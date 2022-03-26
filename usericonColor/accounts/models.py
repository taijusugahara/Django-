from django.db import models
from django.contrib.auth.models import(
  BaseUserManager,AbstractBaseUser,PermissionsMixin
)
# Create your models here

from django.urls import reverse_lazy

def get_usercolor():#色を順番に付与してあげる
#   最新のuserを削除したときに色がずれる(lastのpkがずれるため) ただし前後のユーザーと色がかぶる事はないので大丈夫
  colors = ["red","blue","#21c95d","yellow","black"]
  last_user = Users.objects.all().order_by('-pk').first()
  if last_user:
    user_last_pk = last_user.pk
  else:#userが存在しない場合(最初のユーザー登録時など)
    user_last_pk = 0
  colors_index = user_last_pk % len(colors)
  color = colors[colors_index]
  return color

  #管理画面でユーザーを作成するときに色を付与する処理はadmin.pyでする

class UserManager(BaseUserManager):
  def create_user(self,username,email,password=None):

    if not email:
      raise ValueError('Enter Email')
    user = self.model(
      username = username,
      email = email
    )
    user.set_password(password)
    user.is_superuser = True
    user.save(using=self._db)
    return user

  def create_superuser(self, username, email, password=None):
      user = self.model(
          username=username,
          email=email,
      )
      color = get_usercolor()
      user.color = color
      user.set_password(password)
      user.is_staff = True
      user.is_active = True
      user.is_superuser = True
      user.save(using=self._db)
      return user

  def save():
    color = get_usercolor()
    print(color)


class Users(AbstractBaseUser,PermissionsMixin):
  username = models.CharField(max_length=150)
  email = models.EmailField(max_length=255,unique=True)
  color = models.CharField(blank=True,null=True,max_length=150)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def get_absolute_url(self):
      return reverse_lazy('accounts:home')
  

