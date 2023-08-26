from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('uuid', 'buyer', 'item', 'quantity', 'created_at', 'updated_at')

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)

    def view(self, validated_data):
        return Transaction.objects.all(**validated_data)