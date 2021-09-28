from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

from .models import User 


class UserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    list_filter = ('email', 'username', 'first_name', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name',)
    list_display = ('email', 'username', 'first_name',
                    'is_staff', 'is_active',) 

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups',)}),
    )

    formfield_overrides = {
        User.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(User, UserAdminConfig)
