from rest_framework import serializers

from server.apps.adviser.api.serializers import CategoryDefaultSerializer
from server.apps.adviser.models import Link


class LinkUserSerializer(serializers.ModelSerializer):
    source_name = serializers.CharField(source='get_source_display')
    category = CategoryDefaultSerializer()

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'source', 'source_name', 'category', 'created_at', 'updated_at']