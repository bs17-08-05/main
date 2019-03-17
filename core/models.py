from datetime import datetime

from django.db import models


class Horecama(models.Model):
    HORECAMA_TYPE_CHOICES = (
        ('H', 'Hotel'),
        ('R', 'Restaurant'),
        ('C', 'Cafe'),
        ('M', 'Markets'),
    )
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    photo = models.ImageField(upload_to='horecama/', blank=True)
    type = models.CharField(choices=HORECAMA_TYPE_CHOICES, max_length=1)
    description = models.CharField(max_length=1024)


class Goods(models.Model):
    class Meta:
        verbose_name_plural = "Goods"
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='goods/', blank=True)
    horecama = models.ForeignKey('Horecama', on_delete=models.CASCADE, related_name='menu')
    description = models.CharField(max_length=1024)
    price = models.PositiveIntegerField()


class Order(models.Model):
    time = models.DateTimeField(default=datetime.now, blank=True)
    user_name = models.CharField(max_length=128)
    user_phone = models.CharField(max_length=12)
    address = models.CharField(max_length=512)
    delivered = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    goods = models.ManyToManyField('Goods', related_name='orders', through='GoodsQuantityOrder')
    change_key = models.CharField(max_length=16, blank=True)


class GoodsQuantityOrder(models.Model):
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey('Order', related_name='goods_quantity', on_delete=models.CASCADE)
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)