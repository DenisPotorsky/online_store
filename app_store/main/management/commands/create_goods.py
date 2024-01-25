from django.core.management.base import BaseCommand

# from app_store.main.models import Client
from main.models import Goods
from decimal import Decimal

class Command(BaseCommand):
    help = "Create goods."

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('description')
        parser.add_argument('price')
        parser.add_argument('quantity')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = Decimal(kwargs['price'])
        quantity = kwargs['quantity']
        goods = Goods(name=name, description=description, price=price, quantity=quantity)
        goods.save()
        self.stdout.write(f'{goods}')

