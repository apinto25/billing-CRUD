from django.contrib import admin
from apps.bill.models.bill import Bill
from apps.bill.models.bill_product import BillProduct


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('code', 'date', 'quantity_product', 'total_price', 'payment_method')


@admin.register(BillProduct)
class BillProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_id', 'product_id')
