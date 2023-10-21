from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("email",)
    list_per_page = 30
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_superuser", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )
