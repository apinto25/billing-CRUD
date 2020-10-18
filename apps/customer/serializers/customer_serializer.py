from rest_framework import serializers

from apps.customer.models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Customer
        fields = ["id_number", "name", "last_name", "address", "phone", "photo"]
