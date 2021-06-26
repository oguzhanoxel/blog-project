from ..models import Post
from .serializers import PostSerializer

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)


class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetrieveUpdatePost(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer