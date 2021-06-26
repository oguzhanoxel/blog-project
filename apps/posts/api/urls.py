from django.urls import path

from .views import (
    ListPost,
    RetrievePost,
    CreatePost,
    RetrieveUpdatePost,
    DeletePost)

urlpatterns = [
    path('', ListPost.as_view()),
    path('<int:pk>', RetrievePost.as_view()),
    path('create', CreatePost.as_view()),
    path('<int:pk>/update', RetrieveUpdatePost.as_view()),
    path('<int:pk>/delete', DeletePost.as_view()),
]
