from django.db.models import fields
from rest_framework import serializers

from ..models import Post
from apps.users.api.serializers import UserSerializer


class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at']


class PostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'slug', 'created_at', 'updated_at']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']