from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer, TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as _TokenObtainPairView

User = get_user_model()

class ObtainTokenPairView(_TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer


class RegisterView(CreateAPIView):
    authentication_classes = []
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer