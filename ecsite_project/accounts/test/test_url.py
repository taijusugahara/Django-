from audioop import reverse
from django.test import TestCase
from django.urls import resolve, reverse
from .. import views

class TestUrls(TestCase):
  #クラスベースビュー
  """home ページへのURLでアクセスする時のリダイレクトをテスト"""
  def test_post_home_url(self):
    view = resolve('/accounts/home/')
    self.assertEqual(view.func.view_class, views.HomeView)


  """home name ページへのURLでアクセスする時のリダイレクトをテスト"""
  def test_post_home_url_name(self):
    view = reverse('accounts:home')
    self.assertEqual(resolve(view).func.view_class, views.HomeView)
  

  #関数ベースビュー
  def test_post_home_url_func_view(self):
    view = resolve('/accounts/func_view/')
    self.assertEqual(view.func, views.func_view)

  def test_post_home_url_func_view_name(self):
    view = reverse('accounts:func_view')
    self.assertEqual(resolve(view).func, views.func_view)