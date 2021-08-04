from apps.users.api.views import RetrieveUser
from django.urls.conf import path


urlpatterns = [
    path('<username>/', RetrieveUser.as_view()),
]