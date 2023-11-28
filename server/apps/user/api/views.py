from django.db.models import Prefetch
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from server.apps.adviser.models import Link
from server.apps.user.api.serializers import UserDefaultSerializer, UserDetailSerializer
from server.apps.user.models import User


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all().prefetch_related(
        Prefetch('links', queryset=Link.objects.all().select_related('category'))
    )
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'put', 'patch', 'delete']

    SERIALIZER_CLS = {
        'retrieve': UserDetailSerializer,
        'update': UserDefaultSerializer,
        'partial_update': UserDefaultSerializer,
        'list': UserDefaultSerializer,
        'destroy': UserDefaultSerializer
    }


    def get_serializer_class(self):
        _serializer = self.SERIALIZER_CLS.get(self.action, None)
        if _serializer is not None:
            self.serializer_class = _serializer
        return self.serializer_class
