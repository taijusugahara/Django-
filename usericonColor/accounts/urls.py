from unicodedata import name
from django.urls import path
from .views import(
  RegistUserView, HomeView, UserLoginView,
  UserLogoutView, UserView, asny_test, requests_test, user_all,video,user_all
)

app_name ='accounts'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user/', UserView.as_view(), name='user'),
    path('',asny_test, name="asny"),
    path('req_test',requests_test, name="req"),
    path('video',video, name="video"),

    path('user_all',user_all,name="user_all")
]
