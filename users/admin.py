from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('login', 'email', 'full_name', 'phone', 'is_active', 'is_staff')
    search_fields = ('login', 'email', 'full_name', 'phone')
    list_filter = ('is_active', 'is_staff') 
    list_editable = ('is_active',)


    fieldsets = (
        ('Основная информация', {
            'fields': ('login', 'password', 'email', 'full_name', 'phone')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Важные даты', {
            'fields': ('last_login',)  
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'full_name', 'phone', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('last_login',)  
    ordering = ('login',)  

admin.site.register(User, CustomUserAdmin)