from django.contrib import admin

from .models import Users
from django.contrib.auth.admin import UserAdmin 
from django.utils.translation import gettext as _

def get_usercolor():#色を順番に付与してあげる
#   最新のuserを削除したときに色がずれる(lastのpkがずれるため) ただし前後のユーザーと色がかぶる事はないので大丈夫
  colors = ["red","blue","#21c95d","yellow","black"]
  last_user = Users.objects.all().order_by('-pk').first()
  if last_user:
    user_last_pk = last_user.pk
  else:#userが存在しない場合(最初のユーザー登録時など)
    user_last_pk = 0
  colors_index = user_last_pk % len(colors)
  color = colors[colors_index]
  return color

class UserCreateAdmin(UserAdmin):

    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    def save_model(self, request, obj, form, change):
        if obj.color:
            pass
        else:
            obj.color = get_usercolor()
        super(UserCreateAdmin, self).save_model(request, obj, form, change)

admin.site.register(Users,UserCreateAdmin)