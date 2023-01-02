from django.urls import path
from core.Posts.views import PostRetrieveUpdateDestroyAPIView,PostListCreateAPIView

app_name = "posts"


urlpatterns=[
    path(r'posts/<int:post_id>/',PostRetrieveUpdateDestroyAPIView.as_view()),
    path(r'posts/', PostListCreateAPIView.as_view()),
]


