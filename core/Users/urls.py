from django.urls import path
from core.Users.views import UserListCreateAPIView

app_name = "users"


urlpatterns=[
 path('user/',UserListCreateAPIView.as_view()),

]


