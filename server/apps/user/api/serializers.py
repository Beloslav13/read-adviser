from rest_framework import serializers

from server.apps.adviser.api.serializers.internal import LinkUserSerializer
from server.apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    links = LinkUserSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'links']