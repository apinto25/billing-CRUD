from django.contrib import admin
from apps.customer.models.customer import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'last_name', 'phone', 'address')
