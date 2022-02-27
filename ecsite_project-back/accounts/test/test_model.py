from django.test import TestCase
from accounts.models import Users

class UsersModelTests(TestCase):

  def test_is_empty(self):
      """初期状態では何も登録されていないことをチェック"""  
      users_number = Users.objects.all()
      self.assertEqual(users_number.count(), 0)

  def test_is_empty_false(self):
      """初期状態では何も登録されていないことをチェック"""  
      users_number = Users.objects.all()
      self.assertNotEqual(users_number.count(), 1)

  def test_is_user(self):
    """ユーザーが登録されているかどうか
      save時にオブジェクト生成されるから必要カラムがなくてもsaveされるのか
      バリデーションはformの機能になるんか
    """
    user = Users()
    username = user.username= "testA"
    email = user.email = "test@test.com"
    password = user.password = "xxxxx"
    user.save()
    users_number = Users.objects.all()
    self.assertEqual(users_number.count(), 1)
    one_user = users_number[0]
    self.assertEqual(one_user.username, username)
    self.assertEqual(one_user.email, email)
    self.assertEqual(one_user.is_active, True)
    self.assertEqual(one_user.is_staff, False)
    self.assertEqual(one_user.is_superuser, False)

  def test_is_user_no_input(self):
    """ユーザーが登録されているかどうか"""
    user = Users()
    user.save()
    users_number = Users.objects.all()
    self.assertEqual(users_number.count(), 1)

  def test_many_many_user(self):
    """大量のユーザーを作成"""
    for i in range(10000):
      i = str(i)
      user = Users()
      user.username = "test" + i
      user.email = "test@test" + i + ".com"
      user.password = "xxxxx" + i
      user.save()
    users_number = Users.objects.all()
    self.assertEqual(users_number.count(), 10000)
    self.assertEqual(users_number[5000].username,"test5000")
    self.assertEqual(users_number[5000].email,"test@test5000.com")
    self.assertEqual(users_number[5000].password,"xxxxx5000")
      