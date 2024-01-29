from datetime import datetime, timedelta, date
from itertools import chain
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from . import forms, models
from .forms import ImageForm, ClientForm, GoodForm
from .models import Client, Order, Good


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


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'main/upload_image.html', {'form': form})


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            address = request.POST['address']
            client = Client(name=name, email=email, phone_number=phone_number, address=address)
            client.save()
            return HttpResponse('Пользователь сохранён')
        return HttpResponse('Ошибка валидации')

    else:
        form = ClientForm()
        message = 'Заполните форму клиента'
        return render(request, 'main/add_client.html', {'form': form, 'message': message})


def add_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            quantity = request.POST['quantity']
            image = form.cleaned_data['image']
            good = Good(name=name, description=description, price=price, quantity=quantity, image=image)
            good.save()
            return HttpResponse('Товар сохранён')
        return HttpResponse('Ошибка валидации')

    else:
        form = GoodForm()
        message = 'Заполните форму товара'
        return render(request, 'main/add_good.html', {'form': form, 'message': message})


def update_good(request, pk):
    good = models.Good.objects.filter(pk=pk).first()
    form = forms.GoodForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        good.name = form.cleaned_data['name']
        good.description = form.cleaned_data['description']
        good.price = form.cleaned_data['price']
        good.quantity = form.cleaned_data['quantity']
        good.image = form.cleaned_data['image']
        good.save()
        return HttpResponse('Товар изменен')
    else:
        form = forms.GoodForm(initial={'name': good.name,
                                       'description': good.description,
                                        'price': good.price,
                                       'quantity': good.quantity,
                                       'image': good.image})

    return render(request, 'main/update_good.html', {'form': form})
