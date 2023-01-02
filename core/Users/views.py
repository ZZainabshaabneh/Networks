
from core.serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView

from core.Users.models import User

class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

