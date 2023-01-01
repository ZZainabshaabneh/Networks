from django.urls import path
from core.Users.views import userview,creatuser

app_name = "users"


urlpatterns=[
 path('user/',userview.as_view()),
 path('creatuser/',creatuser.as_view()),
]


