from rest_framework import serializers

from apps.product.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ["code", "category", "name", "price", "quantity", "state",
                  "bill_id"]


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ["category", "name", "price", "quantity", "state", "bill_id"]
