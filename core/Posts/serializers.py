from rest_framework import serializers
from .models import Posts
from .. import Users


class PostsSerializer(serializers.models):

    class Meta:
        model = Posts
        fields = '__all__'


