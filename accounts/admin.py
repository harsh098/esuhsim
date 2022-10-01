from django.contrib.auth.admin import UserAdmin as Useradmin
from .models import User, Hospital, PublicUser
from django.contrib import admin


class UserAdmin(Useradmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'groups', 'user_permissions', 'is_hospital',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', "is_hospital",),

        }),
    )

    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'groups')
    search_fields = ('email', 'username')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)


admin.site.register(Hospital)
admin.site.register(PublicUser)
