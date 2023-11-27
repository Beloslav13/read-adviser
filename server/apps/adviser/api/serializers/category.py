from rest_framework import serializers

from server.apps.adviser.models import Category


class CategorySerializer(serializers.ModelSerializer):
    type_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'type', 'type_name', 'created_at', 'updated_at']

    def get_type_name(self, instance):
        return instance.get_type_display()
