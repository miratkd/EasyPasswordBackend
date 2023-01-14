from django.contrib import admin
from mainApp.models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.


class AccountInline(admin.StackedInline):
    model = Account
    verbose_name_plural = 'Contas'
    verbose_name = 'Conta'
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
