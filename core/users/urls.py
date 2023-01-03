from django.urls import path
from core.users.views import UserListCreateAPIView

app_name = "users"


urlpatterns=[
 path('user/',UserListCreateAPIView.as_view()),

]


