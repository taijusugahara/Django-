from django import forms
from django.core import validators

from . models import Students

class StudentsForm(forms.ModelForm):
  name = forms.CharField(label='名前')
  age = forms.IntegerField(label ='年齢')
  grade = forms.IntegerField(label = '学年')
  picture = forms.FileField(label='画像')

  class Meta:
    model = Students
    fields = '__all__'

  def clean_age(self):
    age = self.cleaned_data['age']
    if age < 18:
       raise validators.ValidationError('年齢は18歳以上の方でお願いします。')
    return age

  def clean_grade(self):
    grade = self.cleaned_data['grade']
    if not 1<= grade <=3:
       raise validators.ValidationError('学年は1から3以外入力できません。')
    return grade

class StudentsUpdateForm(forms.Form):
  name = forms.CharField(label='名前')
  age = forms.IntegerField(label ='年齢')
  grade = forms.IntegerField(label = '学年')
  picture = forms.FileField(label='画像',required=False)

class StudentsDeleteForm(forms.Form):
  id = forms.IntegerField(widget=forms.HiddenInput)
