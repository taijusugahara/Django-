from django.urls import path
from . import views

app_name = 'temp_app'
urlpatterns = [
    path('home', views.home, name='home'),
    path('members', views.members, name='members'),
    path('member/<int:id>', views.member, name='member'),
    # path('home/<first_name>/<last_name>', views.home, name='home'),
    # path('sample1', views.sample1, name='sample1'),
    # path('sample2', views.sample2, name='sample2'),
    # path('sample', views.sample, name='sample'),
    # path('sample3', views.sample3, name='sample3'),
]
