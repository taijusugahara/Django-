from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView,FormView
from django.views.generic.base import TemplateView,View
from .forms import RegistForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

import requests
import aiohttp
import asyncio
import time

# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'

async def asny_test(request):
  start_time = time.time()
  pokemon_lists = await main()
  end_time = time.time()
  howlong = end_time - start_time
  print(f"かかった時間: {howlong}")
  return render(request,'home.html',context={
    "lists" : pokemon_lists
  })


async def main():
  lists = []
  poke_lists = []
  async with aiohttp.ClientSession() as session:
    for number in range(1, 100):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        lists.append(asyncio.ensure_future(get_pokemon(session, url)))
        # async with session.get(pokemon_url) as resp:
        #     pokemon = await resp.json()
        #     print(pokemon['name'])
        #     lists.append(pokemon['name'])
    original_pokemon = await asyncio.gather(*lists)
    for pokemon in original_pokemon:
      print(pokemon)
      poke_lists.append(pokemon)

  return poke_lists

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


def requests_test(request):
  start_time = time.time()
  for number in range(1, 2):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])
    end_time = time.time()
    howlong = end_time - start_time
    print(f"かかった時間requests: {howlong}")
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