from django.urls import path
from . import views

app_name='file'

urlpatterns = [
  path('', views.file_upload, name='file_upload'),
  path('success',views.success,name="success")
]