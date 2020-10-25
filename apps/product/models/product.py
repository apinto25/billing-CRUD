from django.db import models


class Product(models.Model):
    code = models.IntegerField('Product code', primary_key=True)
    category = models.CharField('Category', max_length=250)
    name = models.CharField('Product name', max_length=250)
    price = models.CharField('Price', max_length=250)
    quantity = models.IntegerField('Quantity')
    state = models.BooleanField('Product state', help_text='True for active, False for Inactive')
    bill_id = models.ManyToManyField('bill.Bill', through='bill.BillProduct')
