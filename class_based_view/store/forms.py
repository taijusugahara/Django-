from django import forms
from django.db.models.fields.files import FileField
from .models import Books,Pictures
from datetime import datetime

class BookForm(forms.ModelForm):
  
  class Meta:
    model = Books
    fields = ['name','description','price']

  def save(self, *args, **kwargs):
    obj = super(BookForm,self).save(commit=False) #booksクラスのインスタンス
    obj.created_at = datetime.now()
    obj.update_at = datetime.now()
    obj.save()
    return obj



class BookUpdateForm(forms.ModelForm):
  
  class Meta:
    model = Books
    fields = ['name','description','price',]

  def save(self, *args, **kwargs):
    obj = super(BookUpdateForm,self).save(commit=False) #booksクラスのインスタンス
    obj.update_at = datetime.now()
    obj.save()
    return obj


class PictureUploadForm(forms.ModelForm):
  picture = forms.FileField(required=False)

  class Meta:
    model = Pictures
    fields = ['picture',]

  def save(self,*args,**kwargs):
    obj = super(PictureUploadForm,self).save(commit=False)
    obj.created_at = datetime.now()
    obj.update_at = datetime.now()
    obj.book = kwargs['book']
    obj.save()
    return obj


