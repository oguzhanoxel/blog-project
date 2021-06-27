from django.contrib.auth import get_user_model, login

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView

from .permissions import IsOwner
from .serializers import UserSerializer, UserDetailSerializer

User = get_user_model()


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    lookup_field = 'id'

# {
#     "username": "admin",
#     "email": "admin@bot.com",
#     "password": "Password@123"
# }

class RegisterAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# {
#     "username": "user",
#     "password": "123456"
# }

class LoginAPI(KnoxLoginView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class RetrieveUpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    lookup_field = 'id'


class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwner]
    serializer_class = UserSerializer
    lookup_field = 'id'