from rest_framework import serializers

from server.apps.adviser.api.serializers import CategoryDefaultSerializer
from server.apps.adviser.models import Link
from server.apps.user.api.serializers import UserDefaultSerializer


class LinkDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'category']

class LinkListOrDetailSerializer(serializers.ModelSerializer):
    owner = UserDefaultSerializer()
    category = CategoryDefaultSerializer()

    class Meta:
        model = Link
        fields = ['id', 'name', 'url', 'owner', 'category', 'created_at', 'updated_at']
