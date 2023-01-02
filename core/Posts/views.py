from core.Posts.serializers import PostsSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from core.Posts.models import Posts



class PostListCreateAPIView(ListCreateAPIView):
      model=Posts

      queryset = Posts.objects.all()
      serializer_class = PostsSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

