from django.shortcuts import render
from . import forms
from django.http.response import JsonResponse
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
  return render(request,'success.html')