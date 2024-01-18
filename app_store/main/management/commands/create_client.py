from django.core.management.base import BaseCommand

# from app_store.main.models import Client
from main.models import Client


class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('name')
        parser.add_argument('email')
        parser.add_argument('number')
        parser.add_argument('address')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        number = kwargs['number']
        address = kwargs['address']
        client = Client(name=name, email=email, phone_number=number, address=address)
        client.save()
        self.stdout.write(f'{client}')
