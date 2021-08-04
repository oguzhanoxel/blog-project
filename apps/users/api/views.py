from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.users.api.serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RetrieveUser(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(RetrieveUser, self).dispatch(*args, **kwargs)
