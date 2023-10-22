from django.contrib import admin
from apps.users.models import User, LoginHistory


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_per_page = 30
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_superuser", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "user", "successful", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )
