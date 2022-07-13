from django.test import TestCase, Client
from django.contrib.admin.sites import AdminSite
from accounts.models import Users

class AdminTests(TestCase):
  def setUp(self):
    user = Users.objects.create_user("test","test@test.com","testuser")

  def test_admin_login(self):
    self.site = AdminSite()
    self.client = Client()
    self.client.login(username='test', password='testuser')