from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from server.apps.user.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """Класс админки пользователя."""

    list_display = ('id', 'email', 'username', 'telegram_username', 'last_name', 'first_name', 'is_superuser', 'is_active')
    search_fields = ('last_name', 'first_name', 'username', 'telegram_username', 'email',)
    list_filter = ('telegram_username', 'is_superuser', 'is_active')
    ordering = ('id', 'email', 'username', 'last_name', 'first_name', 'is_superuser')
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2', 'email', 'telegram_username'),
            },
        ),
    )
