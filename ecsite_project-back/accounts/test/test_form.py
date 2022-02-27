from django.test import TestCase
from accounts.models import Users
from accounts.forms import RegistForm
from django.core.exceptions import ValidationError

#formテストからモデルを調べることもできる
class FormUserRegistTest(TestCase):
  """ユーザー登録テスト
  関数の頭にtestをつけないと動かないです
  """
  def test_correct_form(self):
    username = 'SampleUser'
    age = 10
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertTrue(form.is_valid())
    
    form.save()
    #こっから
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 1)
    created_user = model_users[0]
    self.assertEqual(created_user.username, username)
    self.assertEqual(created_user.email, email)
    self.assertEqual(created_user.is_active, True)
    self.assertEqual(created_user.is_staff, False)
    self.assertEqual(created_user.is_superuser, False)

  def test_age_word(self):
    """ageが文字"""
    username = 'SampleUser'
    age = "10歳"
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_age_less_0(self):
    """age less than 0"""
    username = 'SampleUser'
    age = "10歳"
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : -1,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_username_length_true(self):
    """username.length less than 150"""
    username = 'i'*150
    age = 10
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    # self.assertTrue(form.is_valid())
    self.assertTrue(form.save())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 1)

  def test_username_length_true(self):
    """username.length more than 150"""
    username = 'i'*151
    age = 10
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    # self.assertFalse(form.save())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_not_correct_email(self):
    """username.length more than 150"""
    username = 'illlgersr'
    age = 10
    email = 'sampleexample.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    # self.assertFalse(form.save())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_not_correct_email2(self):
    """username.length more than 150"""
    username = 'illlgersr'
    age = 10
    email = 'sample@examplecom'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    # self.assertFalse(form.save())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_not_correct_double_email(self):
    """username.length more than 150"""
    username = 'illlgersr'
    age = 10
    email = 'sample@example.com'
    password = "これはパスワードですよおおおおお"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertTrue(form.is_valid())
    self.assertTrue(form.save())
    another_user_form_data = {
            'username': "別ユーザーさん",
            'age' : 10,
            'email': email,
            'password': password,
        }
    form = RegistForm(another_user_form_data)
    self.assertFalse(form.is_valid())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 1)

  def test_password_empty(self):
    """username.length more than 150"""
    username = 'illlgersr'
    age = 10
    email = 'sample@example.com'
    password = ""
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertFalse(form.is_valid())
    model_users = Users.objects.all()
    self.assertEqual(model_users.count(), 0)

  def test_password_too_short(self):
    """username.length more than 150"""
    username = 'illlgersr'
    age = 10
    email = 'sample@example.com'
    password = "x"
    user_form_data = {
            'username': username,
            'age' : age,
            'email': email,
            'password': password,
        }
    form = RegistForm(user_form_data)
    self.assertTrue(form.is_valid())
    ###########
    # save失敗するときの処理はvaldationerror使う
    # raiseするときはwith使って。
    with self.assertRaises(ValidationError):
      form.save()
    with self.assertRaisesMessage(ValidationError, "['This password is too short. It must contain at least 8 characters.', 'This password is too common.']"):
      form.save()
    
    # model_users = Users.objects.all()
    # self.assertEqual(model_users.count(), 0)








