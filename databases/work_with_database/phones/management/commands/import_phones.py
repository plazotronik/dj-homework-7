import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                device = Phone()
                device.id_device = int(line[0])
                device.name = line[1]
                device.image = line[2]
                device.price = int(line[3])
                device.release_date = datetime.fromisoformat(line[4])
                device.lte_exists = line[5]
                device.slug = slugify(device.name, allow_unicode=True)
                device.save()

