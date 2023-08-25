from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('uuid', 'name', 'type', 'regular_price', 'vip_price', 'wholesale_price', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def view(self, validated_data):
        return Item.objects.all(**validated_data)
