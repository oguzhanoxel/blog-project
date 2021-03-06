from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework import filters

from ..models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
        PostListSerializer,
        PostDetailSerializer,
        PostCreateUpdateSerializer,
    )


class ListPost(ListAPIView):
    authentication_classes = []
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostListSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        ]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(ListPost, self).dispatch(*args, **kwargs)


class RetrievePost(RetrieveAPIView):
    authentication_classes = []
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostDetailSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(RetrievePost, self).dispatch(*args, **kwargs)


class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class RetrieveUpdatePost(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostCreateUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(author = self.request.user)

class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
    serializer_class = PostDetailSerializer