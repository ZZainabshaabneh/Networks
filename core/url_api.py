
from django.urls import path
from django.conf.urls import include
from .Posts import urls as url_posts
from .Users import urls as url_users


urlpatterns=[
    path('',include(url_users)),
    path('',include(url_posts)),

]