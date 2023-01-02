from django.urls import path
from core.Posts.views import PostRetrieveUpdateDestroyAPIView,PostListCreateAPIView

urlpatterns=[
    path(r'posts/<int:post_id>/',PostRetrieveUpdateDestroyAPIView.as_view()),
    path(r'posts/', PostListCreateAPIView.as_view()),
]


