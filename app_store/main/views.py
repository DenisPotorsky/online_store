from datetime import datetime, timedelta, date
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Order


def index_page(request):
    return render(request, 'main/index.html')


def about_page(request):
    return render(request, 'main/about.html')


def show_clients(request):
    client = Client.objects.all()
    result = '<br>'.join([str(client) for client in client])
    return HttpResponse(result)



def show_sorted_orders(request):
    d = datetime.today() - timedelta(days=2)
    context = {}
    context['orders'] = Order.objects.filter(date_ordered__gte=date(d.year, d.month, d.day))
    return render(request, 'main/sorted_orders.html', context)


def get_client_orders(request, pk):
    orders = Order.objects.filter(client_id=pk)
    li = [order.get_goods() for order in orders]
    sorted_list = list(chain.from_iterable(li))
    return render(request, 'main/orders_and_goods.html', {'orders': orders, 'goods': sorted_list})