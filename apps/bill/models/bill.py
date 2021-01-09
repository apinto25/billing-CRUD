from django.db import models

from apps.customer.models.customer import Customer


PAYMENT_METHODS = [
    ("1", "Credit Card"),
    ("2", "Debit Card"),
    ("3", "Cash"),
]


class Bill(models.Model):
    code = models.IntegerField('Bill code', unique=True)
    date = models.DateTimeField('Date', auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField('Total price', decimal_places=2, max_digits=50)
    payment_method = models.CharField('Payment method', max_length=100, choices=PAYMENT_METHODS)
    quantity_product = models.IntegerField('Quantity of products')
    product_id = models.ManyToManyField('product.Product', through='bill.BillProduct')

    def __str__(self):
        return str(self.code)
