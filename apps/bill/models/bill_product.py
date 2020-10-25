from django.db import models

from apps.bill.models.bill import Bill
from apps.product.models.product import Product


class BillProduct(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
