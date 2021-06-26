from django.urls import path

from .views import (
    ListUser,
    DetailUser,
    RetrieveUpdateUser,
    CreateUser,
    DeleteUser,
)

urlpatterns = [
    path('', ListUser.as_view()),
    path('<int:pk>', DetailUser.as_view()),
    path('create', CreateUser.as_view()),
    path('<int:pk>/update', RetrieveUpdateUser.as_view()),
    path('<int:pk>/delete', DeleteUser.as_view()),
]
