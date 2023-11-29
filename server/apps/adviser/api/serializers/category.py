from rest_framework import serializers

from server.apps.adviser.models import Category


class CategoryDefaultSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'type', 'type_name', 'created_at', 'updated_at']


class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'type']
