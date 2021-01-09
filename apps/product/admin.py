from django.contrib import admin
from apps.product.models.product import Product
from apps.product.models.category import Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'category', 'name', 'price', 'quantity', 'state')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
