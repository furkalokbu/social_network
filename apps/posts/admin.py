from django.contrib import admin
from apps.posts.models import Post, RequestHistory


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "title", "body", "author", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(RequestHistory)
class RequestHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "method", "path", "created_at")
    readonly_fields = ("created_at", "updated_at",)
