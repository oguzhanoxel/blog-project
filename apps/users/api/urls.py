from django.urls import path

from knox import views as knox_views

from .views import (
    ListUser,
    LoginAPI,
    RegisterAPI,
    DetailUser,
    RetrieveUpdateUser,
    DeleteUser,
)

urlpatterns = [
    path('', ListUser.as_view()),
    path('<int:id>', DetailUser.as_view()),
    path('register', RegisterAPI.as_view()),
    path('login', LoginAPI.as_view()),
    path('logout', knox_views.LogoutView.as_view()),
    path('logoutall', knox_views.LogoutAllView.as_view()),
    path('<int:id>/update', RetrieveUpdateUser.as_view()),
    path('<int:id>/delete', DeleteUser.as_view()),
]
