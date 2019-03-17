from rest_framework.serializers import ModelSerializer, RelatedField

from core.models import Order, GoodsQuantityOrder


def goods_quantity_order_serializer(goods_quantity_order):
    return {'id': goods_quantity_order.goods.id, 'quantity': goods_quantity_order.quantity}


def order_serializer(order):
    return {'id': order.id, 'user_name': order.user_name, 'user_phone': order.user_phone, 
           'address': order.address, 'price': order.price, 
           'goods_quantity': [goods_quantity_order_serializer(i) for i in order.goods_quantity.all()]}