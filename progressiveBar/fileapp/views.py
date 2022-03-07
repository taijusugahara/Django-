# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from . import forms
from django.http.response import JsonResponse
from .models import File
import os
from django.http import HttpResponse
# Create your views here.

def file_upload(request):
  form = forms.FileUpload()

  if request.method == 'POST':
    d={}
    form = forms.FileUpload(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      d['is_ok'] = "ok"
    else:
      print(form.errors)
      d['is_ok'] = 'no'
      d['errors'] = form.errors
    return JsonResponse(d)

  return render(request,'index.html',context={
    'form' : form
  })

def success(request):
  files = File.objects.all()

  return render(request,'success.html',context={
    'files' : files
  })

def filename_update(request):
  files = File.objects.all()

  if request.method == 'POST':
    id = request.POST['id']
    filename = request.POST['filename']

    file_obj = File.objects.get(pk=id)

    file_before_name = file_obj.file.name

    file_same_obj = File.objects.filter(file=filename)
    if file_same_obj:
      return HttpResponse("そのファイル名は使用されています。別のファイル名を使用ください。")
    else:
      file_obj.file.name = filename
      file_obj.save()
      os.rename("media/" + file_before_name,"media/" + filename)



  return render(request,'success.html',context={
  'files' : files
  })