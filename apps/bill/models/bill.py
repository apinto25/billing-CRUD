from django.db import models

from apps.customer.models.customer import Customer


class Bill(models.Model):
    code = models.IntegerField('Bill code', primary_key=True)
    date = models.DateTimeField('Date', auto_now_add=True)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.CharField('Total price', max_length=250)
    payment_method = models.CharField('Payment method', max_length=100)
    quantity_product = models.IntegerField('Quantity of products')
    product_id = models.ManyToManyField('product.Product', through='bill.BillProduct')
