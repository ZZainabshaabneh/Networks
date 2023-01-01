from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import UserSerializer, GroupSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.views.generic import ListView
from core.Users.models import User,Address,Relation
from django.views.generic import DetailView
class userview(DetailView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class creatuser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

