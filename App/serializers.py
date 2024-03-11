from rest_framework import serializers
from .models import PostModel, UserModel


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username"]


# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    username = UserSerializer()

    class Meta:
        model = PostModel
        fields = ["id", "username", "created_datetime", "title", "content"]
