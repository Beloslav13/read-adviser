from rest_framework import viewsets, permissions

from server.apps.user.api.serializers import UserSerializer
from server.apps.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
