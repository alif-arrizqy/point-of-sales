from rest_framework import serializers
from .models import User


class FindNameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'name', 'type', 'created_at', 'updated_at')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def view(self, validated_data):
        return User.objects.all(**validated_data)
