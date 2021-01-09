import os
import uuid

from django.db import models


def customer_image_file_path(instance, file_name):
    """Generate file path for new customer image"""
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/', file_name)


class Customer(models.Model):
    id_number = models.IntegerField('ID number', unique=True)
    name = models.CharField('Name', max_length=250)
    last_name = models.CharField('Last name', max_length=250)
    address = models.CharField('Address', max_length=250)
    phone = models.BigIntegerField('Phone number')
    photo = models.ImageField('Profile photo', upload_to=customer_image_file_path, blank=True, null=True)
