from rest_framework import serializers

from server.apps.adviser.api.serializers import CategoryDefaultSerializer
from server.apps.adviser.models import Link
from server.apps.user.api.serializers import UserDefaultSerializer


class LinkDefaultSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='get_source_display', read_only=True, required=False)

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'source', 'source_name', 'rating', 'category']


class LinkListOrDetailSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='get_source_display', read_only=True, required=False)
    owner = UserDefaultSerializer()
    category = CategoryDefaultSerializer()

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'source', 'source_name', 'category', 'rating', 'created_at', 'updated_at']
