from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'name', 'surname', 'cell_phone', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'name', 'surname', 'cell_phone')
    readonly_fields = ('data_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)