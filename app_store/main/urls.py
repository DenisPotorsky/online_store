from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),
    path('clients/', views.show_clients, name='clients'),
    path('sorted/', views.show_sorted_orders, name='sorted'),
    path('client_orders/<int:pk>/', views.get_client_orders, name='client_orders'),
    path('upload/', views.upload_image, name='upload_image'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_good/', views.add_good, name='add_good'),
    path('update_good/<int:pk>', views.update_good, name='update_good'),
]
