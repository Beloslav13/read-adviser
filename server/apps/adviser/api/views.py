from rest_framework import viewsets, permissions

from server.apps.adviser.api.serializers import CategorySerializer, LinkSerializer
from server.apps.adviser.models import Category, Link


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]
