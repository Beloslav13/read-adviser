from rest_framework import serializers

from server.apps.adviser.api.serializers import CategorySerializer
from server.apps.adviser.models import Link
from server.apps.user.api.serializers import UserSerializer


class LinkSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'category', 'created_at', 'updated_at']