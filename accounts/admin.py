from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = (
        'id',
        'first_name', 
        'last_name', 
        'username', 
        'email', 
        'last_login', 
        'is_admin', 
        'is_active', 
        'date_joined',
        )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display_links = ('username', )
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined', )
    
admin.site.register(Account, AccountAdmin)