
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

from ..models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
        PostListSerializer,
        PostDetailSerializer,
        PostCreateUpdateSerializer,
    )



class ListPost(ListAPIView):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostListSerializer


class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer


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