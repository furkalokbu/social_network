from rest_framework import serializers
from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'body', 'liked', 'author', 'created_at')
        read_only_fields = ('updated_at', 'created_at', 'author')
