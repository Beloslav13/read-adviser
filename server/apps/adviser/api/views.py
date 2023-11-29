from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from server.apps.adviser.api.serializers import (
    CategoryDefaultSerializer,
    LinkDefaultSerializer,
    LinkListOrDetailSerializer,
    CategoryUpdateSerializer
)
from server.apps.adviser.models import Category, Link
from server.q import query_debugger


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Category.objects.all()
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    SERIALIZER_CLS = {
        'create': CategoryDefaultSerializer,
        'retrieve': CategoryDefaultSerializer,
        'update': CategoryUpdateSerializer,
        'partial_update': CategoryUpdateSerializer,
        'list': CategoryDefaultSerializer,
        'destroy': CategoryDefaultSerializer
    }

    def get_serializer_class(self):
        _serializer = self.SERIALIZER_CLS.get(self.action, None)
        if _serializer is not None:
            self.serializer_class = _serializer
        return self.serializer_class


class LinkViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Link.objects.all().select_related('category', 'owner')
    serializer_class = None
    permission_classes = [permissions.IsAuthenticated]

    SERIALIZER_CLS = {
        'create': LinkDefaultSerializer,
        'retrieve': LinkListOrDetailSerializer,
        'update': LinkDefaultSerializer,
        'partial_update': LinkDefaultSerializer,
        'list': LinkListOrDetailSerializer,
        'destroy': LinkDefaultSerializer
    }


    def get_serializer_class(self):
        _serializer = self.SERIALIZER_CLS.get(self.action, None)
        if _serializer is not None:
            self.serializer_class = _serializer
        return self.serializer_class

    @query_debugger
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @query_debugger
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

