from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Profile


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'firstname', 'lastname', 'role')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('firstname', 'lastname', 'email',
         'phonenumber', 'school_unique_id', 'date_of_birth', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'firstname', 'lastname', 'email', 'phonenumber', 'school_unique_id', 'date_of_birth', 'role'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
