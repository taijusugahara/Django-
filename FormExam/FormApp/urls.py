from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
  path('index/',views.index,name='index'),
  path('create/',views.create,name='create'),
  path('multi_create/',views.multi_create,name='multi_create'),
  path('update/<int:id>',views.update,name='update'),
  path('delete/<int:id>',views.delete,name='delete'),
  path('destroy/<int:id>',views.destroy,name='destroy'),
]