from django.contrib import admin
from .models import Horecama, Goods, Order, GoodsQuantityOrder


# Register your models here.
admin.site.register(Horecama)
admin.site.register(Goods)
admin.site.register(Order)
admin.site.register(GoodsQuantityOrder)
