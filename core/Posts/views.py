from core.Posts.serializers import PostsSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from core.Posts.models import Posts



class CreatPost(ListCreateAPIView):
      model=Posts

      queryset = Posts.objects.all()
      serializer_class = PostsSerializer

class APIPosts(ListCreateAPIView):

    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class DeletePost(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


class UpdatePost(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

