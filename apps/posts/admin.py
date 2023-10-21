from django.contrib import admin
from apps.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ("id", "title", "body", "author", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
    )
