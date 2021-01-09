from rest_framework import serializers

from apps.bill.models.bill import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta():
        model = Bill
        fields = ["code", "date", "customer", "total_price", "payment_method",
                  "quantity_product", "product_id"]
