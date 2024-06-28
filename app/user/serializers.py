from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    createDatetime = serializers.DateTimeField(source="create_datetime", format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["uuid", "name", "createDatetime"]
