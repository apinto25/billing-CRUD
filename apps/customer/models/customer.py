from django.db import models


def customer_image_file_path(instance, file_name):
    """Generate file path for new customer image"""
    ext = file_name.split('.')[-1]
    file_name = f'{uuid.uuid4()}.{ext}'

    return os.path.join('images/', file_name)


class Customer(models.Model):
    id_number = models.IntegerField('Cedula', primary_key=True)
    name = models.CharField('Nombre', max_length=250)
    last_name = models.CharField('Apellido', max_length=250)
    address = models.CharField('Dirección', max_length=250)
    phone = models.BigIntegerField('Celular')
    photo = models.ImageField('Imagen', upload_to='images/', blank=True, null=True)
