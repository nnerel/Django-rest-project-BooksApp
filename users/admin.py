from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

from .models import NewUser 


class UserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    list_filter = ('email', 'user_name', 'first_name', 'is_staff', 'is_active')
    search_fields = ('email', 'user_name', 'first_name',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_staff', 'is_active',) 

    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
          #  'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(NewUser, UserAdminConfig)
