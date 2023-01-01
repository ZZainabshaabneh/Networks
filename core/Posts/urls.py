from django.urls import path
from core.Posts.views import CreatPost,APIPosts,DeletePost,UpdatePost

app_name = "posts"


urlpatterns=[
    path(r'posts/all/deletepost/<int:post_id>/',DeletePost.as_view()),
    path(r'posts/all/updatepost/<int:post_id>/', UpdatePost.as_view()),
    path(r'posts/all/<int:post_id>/creatpost/', CreatPost.as_view()),
    path(r'posts/', APIPosts.as_view()),



]


