from django.contrib import admin
from .models import Client, Good, Order


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    list_editable = ['email', 'phone_number', 'address', ]
    list_filter = ['registration_date']
    search_fields = ['name', 'email', 'phone_number', 'address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price']


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'image']
    list_editable = ['description', 'price', 'quantity', 'image']
    search_fields = ['name', 'description', 'price', 'quantity']
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],

            },
        ), (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            })
        , ]







