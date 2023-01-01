from django.contrib.auth.models import  Group
from rest_framework import serializers
from .models import Posts
from .. import Users


class PostsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']