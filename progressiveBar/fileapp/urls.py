from unicodedata import name
from django.urls import path
from . import views

app_name='file'

urlpatterns = [
  path('', views.file_upload, name='file_upload'),
  path('success/',views.success,name="success"),
  path('filename_update/',views.filename_update,name="filename_update")
]