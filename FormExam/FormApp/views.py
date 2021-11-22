from django.shortcuts import render
from django.forms import modelformset_factory
from django.core.files.storage import FileSystemStorage
import os

from . import forms
from . import models

# Create your views here.
def index(request):
  students = models.Students.objects.all()
  return render(request,'index.html',context={
    'students':students})


def create(request):
  form = forms.StudentsForm()
  if request.method == 'POST':
    form = forms.StudentsForm(request.POST,request.FILES)
    if form.is_valid():
      form.save()
  return render(request,'create.html',context={
    'form':form})

def multi_create(request):
  Formset = modelformset_factory(models.Students, fields='__all__', extra=3, max_num=3)
  formset = Formset(request.POST or None, request.FILES or None, queryset = models.Students.objects.filter(name=""))
  if formset.is_valid():
    formset.save()
  return render(request,'multi_create.html',context={
    'form':formset})

def update(request,id):
  student = models.Students.objects.get(id=id)
  form = forms.StudentsUpdateForm( initial={
    'name':student.name,
    'age':student.age,
    'grade':student.grade,
    'picture':student.picture
  })
  if request.method =='POST':
    update_form = forms.StudentsUpdateForm(request.POST,request.FILES)
    if update_form.is_valid():
      student.name = update_form.cleaned_data['name']
      student.age = update_form.cleaned_data['age']
      student.grade = update_form.cleaned_data['grade']
      #画像はデフォルトで何も選択されていない。画像を変える必要がない場合に備えて画像を選択した時だけpictureを書き換えるようにする
      picture = update_form.cleaned_data['picture']
      if picture:
    #   fs = FileSystemStorage()
    #   file_name = fs.save(os.path.join('student',picture.name),picture)
      # student.picture = file_name
       student.picture = picture
      student.save()

      
  return render(request,'update.html', context={
    'form':form,
    'student':student #deleteしたい時などidが必要な時に使える！
  })
  

def delete(request,id):
  delete_form = forms.StudentsDeleteForm(
    initial ={
      'id':id
    }
  )
  if request.method=='POST':
    delete_form = forms.StudentsDeleteForm(request.POST or None)
    if delete_form.is_valid():
      models.Students.objects.get(id = delete_form.cleaned_data['id']).delete()
    
  return render(request,'delete.html',context={
    'form':delete_form
  })

#フォーム使わない
def destroy(request,id):
  models.Students.objects.get(id =id).delete()
  return render(request,'destroy.html')