from django.core.management.base import BaseCommand

# from app_store.main.models import Client
from main.models import Order, Client, Goods


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client_id')
        parser.add_argument('total_price')
        parser.add_argument('good_id')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(id=kwargs['client_id'])
        total_price = kwargs['total_price']
        order = Order(client=client, total_price=total_price)
        order.save()
        goods_to_add = Goods.objects.get(id=kwargs['good_id'])
        order.goods.add(goods_to_add)
        self.stdout.write(f'{order}')
