from accounts import views
from accounts.models import Users
from django.test import TestCase, Client
from django.contrib import auth

class ViewTest(TestCase):
  def setUp(self):
    user = Users.objects.create_user("test","test@test.com","testuser")
    self.client = Client()
  def test_login(self):
    response = self.client.post(
      '/accounts/user_login/',
      {'username': 'test@test.com','password' : "testuser",}
    )
    self.assertRedirects(response, '/accounts/home/')
    self.assertIn('_auth_user_id', self.client.session)
    self.assertTrue(self.client.session['_auth_user_id'],1)

    response2 = self.client.get("/accounts/calender")
    self.assertEqual(response2.status_code,200)
  def test_login_fail(self):
    response = self.client.post(
      '/accounts/user_login/',
      {'username': 'test11@test.com','password' : "testusdder",}
    )
    self.assertNotEqual(response.status_code,302)
    self.assertNotIn('_auth_user_id', self.client.session)
    response2 = self.client.get("/accounts/calender")
    self.assertNotEqual(response2.status_code,200)
