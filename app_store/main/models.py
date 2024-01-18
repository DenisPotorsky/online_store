from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=255, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone_number} {self.address} {self.registration_date}'


class Goods(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_of_addition = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.quantity} {self.date_of_addition}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return f'{self.client} {self.goods} {self.date_ordered} {self.total_price}'
