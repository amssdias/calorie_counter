from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models.user import User

class UserAdminCustom(UserAdmin):
   list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser')
   list_filter = ('is_staff', 'is_superuser')
   search_fields = ('username', 'email')


admin.site.register(User, UserAdminCustom)