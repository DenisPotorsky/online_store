from django.shortcuts import render
from django.http import HttpResponse

from .models import Client


#
# def index_page(request):
#     return render(request, 'index.html')
#
#
# def about_page(request):
#     return render(request, 'about.html')


def show_clients(request):
    client = Client.objects.all()
    result = '<br>'.join([str(client) for client in client])
    return HttpResponse(result)


def index_page(request):
    text_i = ('<h1>Главная<h1> <br> <p>Скорее всего это будет сайт магазина-мастерской '
              'с онлайн записью и многим другим</p>')
    return HttpResponse(text_i)


def about_page(request):
    text_a = ('<h1>О нас<h1> <br> <p>Меня зовут Щанников Денис Анатольевич, 47 лет. Я концертный форепианный техник, '
              'ну или по-простому настройщик пианино и роялей.</p>')
    return HttpResponse(text_a)



