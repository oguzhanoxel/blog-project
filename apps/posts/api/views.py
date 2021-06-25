from ..models import Post
from .serializers import PostSerializer

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer