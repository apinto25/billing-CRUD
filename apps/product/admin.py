from django.contrib import admin
from apps.product.models.product import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'category', 'name', 'price', 'quantity', 'state')
