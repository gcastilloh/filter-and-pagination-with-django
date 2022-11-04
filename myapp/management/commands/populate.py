from django.core.management import BaseCommand
from faker import Faker

from myapp.models import Product
from random import randrange

class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()
        print('Adding 500 records to Products model')
        print(f'Before we have: {Product.objects.all().count()} products')
        for _ in range(500):
            Product.objects.create(
                title = faker.name(),
                description = faker.text(200),
                image = faker.image_url(),
                price = randrange(10,100),
            )
        print(f'Now we have: {Product.objects.all().count()} products')
