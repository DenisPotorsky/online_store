from django.shortcuts import render
from django.http import HttpResponse


def index_page(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')

# text_i = '<h1>Главная<h1> <br> <p>всякий текст, много текста по заданию о сайте</p>'
# text_a = '<h1>О нас<h1> <br> <p>всякий текст, много текста по заданию о нас</p>'
#
#
# def index_page(request):
#     return HttpResponse(text_i)
#
# def about_page(request):
#     return HttpResponse(text_a)
