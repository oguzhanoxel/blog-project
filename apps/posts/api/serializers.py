from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'slug', 'created_at', 'updated_at']