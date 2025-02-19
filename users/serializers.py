from rest_framework.serializers import ModelSerializer

from users.models import User


class UserInputSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserOutputSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]
