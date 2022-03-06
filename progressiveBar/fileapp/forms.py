from turtle import title
from django import forms
from .models import File
# from django.core.exceptions import ValidationError


class FileUpload(forms.ModelForm):
  title = forms.CharField(max_length=20)
  file = forms.FileField()
  
  class Meta:
       model  = File
       fields = ['title','file']

  def clean_title(self):
    title = self.cleaned_data['title']
    if len(title) >= 20:
      raise forms.ValidationError('タイトルは２０文字以内でお願いします。')
    return title

  def clean_file(self):
    file = self.cleaned_data['file']
    file_size = file.size
    if file_size > 10000000000:
      print("ファイル大きい")
      raise forms.ValidationError('ファイルサイズが大きすぎます。')
    return file

  # def clean(self):
  #   cleaned_data = super().clean()
  #   file = cleaned_data["file"]
  #   file_size = file.size
  #   if file_size > 100000:
  #     print("ファイル大きい")
  #     raise forms.ValidationError('ファイルサイズが大きすぎます。')

  def save(self, *args,**kwargs):
    obj = super(FileUpload,self).save(commit=False, *args,**kwargs)
    obj.save()
    return obj
