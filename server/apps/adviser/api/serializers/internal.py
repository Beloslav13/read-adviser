from rest_framework import serializers

from server.apps.adviser.api.serializers import CategorySerializer
from server.apps.adviser.models import Link


class LinkUserSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'category', 'created_at', 'updated_at']