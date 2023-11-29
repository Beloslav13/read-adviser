from rest_framework import serializers

from server.apps.adviser.api.serializers import CategoryDefaultSerializer
from server.apps.adviser.models import Link
from server.apps.user.api.serializers import UserDefaultSerializer


class LinkDefaultSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='get_source_display', read_only=True)
    avg_rate = serializers.FloatField(read_only=True)

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'source', 'source_name', 'avg_rate', 'rating', 'category']


class LinkListOrDetailSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='get_source_display', read_only=True)
    owner = UserDefaultSerializer()
    category = CategoryDefaultSerializer()
    avg_rate = serializers.FloatField(read_only=True)

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'source', 'source_name', 'category', 'rating', 'avg_rate',
                  'created_at', 'updated_at']
