from django.db import models


class Phone(models.Model):
    id_device = models.IntegerField(verbose_name='ID устройства', primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=120)
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(verbose_name='Изображение')
    release_date = models.DateTimeField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(verbose_name='URL', max_length=120, unique=True)

    def __str__(self):
        return self.name