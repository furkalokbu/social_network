from rest_framework import serializers
from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        username = attrs.get("username", "")
        if not username.isalnum():
            raise serializers.ValidationError(
                "The username should only containt alphanumeric characters"
            )

        return attrs

    def create(self, validated_data):
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user
