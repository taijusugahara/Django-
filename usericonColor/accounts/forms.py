from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm


def get_usercolor():#色を順番に付与してあげる
#   最新のuserを削除したときに色がずれる(lastのpkがずれるため) ただし前後のユーザーと色がかぶる事はないので大丈夫
  colors = ["red","blue","green","yellow","black"]
  last_user = Users.objects.all().order_by('-pk').first()
  if last_user:
    user_last_pk = last_user.pk
  else:#userが存在しない場合(最初のユーザー登録時など)
    user_last_pk = 0
  colors_index = user_last_pk % len(colors)
  color = colors[colors_index]
  return color

class RegistForm(forms.ModelForm):
  username = forms.CharField(label="名前")
  age = forms.IntegerField(label='年齢',min_value=0)
  email = forms.EmailField(label='メールアドレス')
  password = forms.CharField(label='パスワード',widget=forms.PasswordInput())

  class Meta:
    model = Users
    fields = ['username','age','email','password']

  def save(self,commit=False):
    user = super().save(commit=False)
    color = get_usercolor()
    user.color = color
    validate_password(self.cleaned_data['password'],user)
    user.set_password(self.cleaned_data['password'])
    user.save()
    return user


# class UserLoginForm(forms.Form):
#   email = forms.EmailField(label='メールアドレス')
#   password = forms.CharField(label='パスワード',widget=forms.PasswordInput())


class UserLoginForm(AuthenticationForm):
  username = forms.EmailField(label='メールアドレス') 
  #usernameはmodelでUSERNAME_FIELDに設定したもの ここではemail
  password = forms.CharField(label='パスワード',widget=forms.PasswordInput())
  remember = forms.BooleanField(label="ログイン状態を保持する", required=False)

