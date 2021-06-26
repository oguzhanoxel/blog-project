from django.contrib.auth import get_user_model

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

from .permissions import IsOwner
from .serializers import UserSerializer, UserDetailSerializer

User = get_user_model()


class ListUser(ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class DetailUser(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    lookup_field = 'id'


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class RetrieveUpdateUser(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    lookup_field = 'id'


class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    lookup_field = 'id'
