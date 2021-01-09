from django.db import models

from apps.product.models.category import Category


class Product(models.Model):
    code = models.IntegerField('Product code', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Product name', max_length=250)
    price = models.DecimalField('Price', decimal_places=2, max_digits=50)
    quantity = models.IntegerField('Quantity')
    state = models.BooleanField('Product state', help_text='True for active, False for Inactive')
    bill_id = models.ManyToManyField('bill.Bill', through='bill.BillProduct')

    def __str__(self):
        return self.name
