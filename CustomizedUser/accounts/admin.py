from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user, get_user_model
from .forms import UserChangeForm, UserCreationForm
from .models import Students, Schools

User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
  form = UserChangeForm #ユーザー編集画面で使うform
  add_form = UserCreationForm #ユーザー作成画面

  #一覧画面で表示する
  list_display = ('username','email','is_staff')

  #ユーザー編集画面で表示する要素
  fieldsets = (
    ('ユーザー情報',{'fields': ('username','email','password','website','picture')}),
    ('パーミッション',{'fields':('is_staff','is_active','is_superuser')}),
  )

  add_fieldsets = (
    ('ユーザー情報',{'fields': ('username','email','password','confirm_password')}),
  )

admin.site.register(User,CustomizeUserAdmin)
# admin.site.register(Students)
# admin.site.register(Schools)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
  fields = ('name','score','age','school') #入力画面で表示するfield(順番)
  list_display = ('id','name','age','score','school') #一覧表示で表示するfield
  list_display_links = ('id',) #編集画面に行くリンク
  search_fields = ('name','age') #検索
  list_filter = ('name','age','score','school') # filterで絞り込み
  list_editable = ('name','age','score') #一覧画面から一気に編集可能になる

@admin.register(Schools)
class SchoolsAdmin(admin.ModelAdmin):
  list_display = ('name','student_count')
  def student_count(self, obj):
    # print(type(obj))
    # print(dir(obj))
    count = obj.students_set.count()
    return count

  student_count.short_description = '生徒数'





