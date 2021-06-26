from django.contrib.auth import get_user_model

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .serializers import UserSerializer

User = get_user_model()


class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateUser(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer