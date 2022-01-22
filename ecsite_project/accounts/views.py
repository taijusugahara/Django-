from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import TemplateView,View
from .forms import RegistForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'

def func_view(request):
  return render(request,'home.html')

class RegistUserView(CreateView):
  template_name = 'regist.html'
  form_class = RegistForm


class UserView(LoginRequiredMixin, TemplateView):
  template_name = 'user.html'

  # @method_decorator(login_required)
  #getでもpostでも実行される
  def dispatch(self,*args,**kwargs):
    return super().dispatch(*args,**kwargs)


#############
# LoginView

class UserLoginView(LoginView):
  template_name = 'user_login.html'
  authentication_form = UserLoginForm

  def form_valid(self,form):
    remember = form.cleaned_data['remember']
    if remember:
      self.request.session.set_expiry(1200000)
    return super().form_valid(form)

############
# LogoutView

class UserLogoutView(LogoutView):
  pass