from rest_framework import serializers


# item serializer
class PricesChildSerializer(serializers.Serializer):
    priceFor = serializers.CharField(max_length=100)
    price = serializers.IntegerField()


class ItemBodySwagger(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    prices = serializers.ListField(child=PricesChildSerializer())

class FindItemSwagger(serializers.Serializer):
    name = serializers.CharField(max_length=100)

# transaction serializer
class BuyerSerializer(serializers.Serializer):
    item = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    buyer = serializers.CharField(max_length=100)


class TransactionBodySwagger(serializers.Serializer):
    transaction = serializers.ListField(child=BuyerSerializer())


# user serializer
class UserBodySwagger(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)

class FindUserSwagger(serializers.Serializer):
    name = serializers.CharField(max_length=100)
