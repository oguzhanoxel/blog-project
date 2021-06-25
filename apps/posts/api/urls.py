from django.urls import path

from .views import (
    PostList,
    PostDetail,
    CreatePost,
    UpdatePost,
    DeletePost)

urlpatterns = [
    path('list', PostList.as_view()),
    path('detail/<int:pk>', PostDetail.as_view()),
    path('create', CreatePost.as_view()),
    path('update/<int:pk>', UpdatePost.as_view()),
    path('delete/<int:pk>', DeletePost.as_view()),
]
