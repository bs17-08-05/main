import random
import string

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.response import Response

from .authentication import Authentication
from delivery_club.decorators import required_fields
from delivery_club.settings import HOST
from .models import Order, Goods, GoodsQuantityOrder, Horecama
from .serializers import order_serializer
from core.serializers.serializers import HorecamaSerializer, GoodsSerializer


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
@authentication_classes((Authentication, ))
@required_fields('user_name', 'user_phone', 'address', 'goods')
def order(request):
    data = request.data
    order = Order(user_name=data['user_name'], user_phone=data['user_phone'], address=data['address'], price=0)
    goods_quantity_dict = {i['id']:int(i['quantity']) for i in data['goods']}
    goods = Goods.objects.filter(id__in=goods_quantity_dict.keys())
    goods_quatities = []
    price = 0
    for good in list(goods):
        quantity = goods_quantity_dict[good.id]
        price += good.price * quantity
    order.price = price
    order.change_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    order.save()
    for good in list(goods):
        gq = GoodsQuantityOrder(quantity=quantity, order=order, goods=good)
        gq.save()
    return Response({'status': 'Ok', 'data': {'change_link': f'http://{HOST}/api/order/{order.id}?key={order.change_key}'}})

  
@api_view(['GET'])
@authentication_classes((Authentication, ))
@renderer_classes((JSONRenderer,))
def get_order(request, id):
    if 'key' not in request.query_params:
        return Response({'status': 'key is required'}, status=400)
    key = request.query_params['key']
    order = get_object_or_404(Order, id=id, change_key=key)
    return Response(order_serializer(order))


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
@authentication_classes((Authentication, ))
@required_fields('user_name', 'user_phone', 'address', 'goods')
def change_order(request, id):
    if 'key' not in request.query_params:
        return Response({'status': 'key is required'}, status=400)
    key = request.query_params['key']
    data = request.data
    
    order = get_object_or_404(Order, id=id, change_key=key)
    order.user_name = data['user_name']
    order.user_phone = data['user_phone']
    order.address = data['address']
    
    # delete all goods related to the order
    GoodsQuantityOrder.objects.filter(order=order).delete()

    goods_quantity_dict = {i['id']:int(i['quantity']) for i in data['goods']}
    goods = Goods.objects.filter(id__in=goods_quantity_dict.keys())
    goods_quatities = []
    price = 0
    for good in list(goods):
        quantity = goods_quantity_dict[good.id]
        gq = GoodsQuantityOrder(quantity=quantity, order=order, goods=good)
        gq.save()
        price += good.price * quantity
    
    order.price = price
    order.change_key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    order.save()
    return Response({'status': 'Ok', 'data': {'change_link': f'http://{HOST}/api/order/{order.id}?key={order.change_key}'}})


@api_view(['DELETE'])
@authentication_classes((Authentication, ))
@renderer_classes((JSONRenderer,))
def delete_order(request, id):
    if 'key' not in request.query_params:
        return Response({'status': 'key is required'}, status=400)
    key = request.query_params['key']
    order = get_object_or_404(Order, id=id, change_key=key)
    order.delete()
    return Response({'status':'Ok'})

  
@api_view(['GET'])
@authentication_classes((Authentication, ))
@renderer_classes((JSONRenderer,))
def get_horecama_list(request):

    qset = Horecama.objects.all()
    json = HorecamaSerializer(qset, many=True, context={'request': request})
    size = len(qset)

    responseData = {
        'data': json.data,
        'size': size,
    }

    response = Response(responseData)
    response["Access-Control-Allow-Origin"] = "*"
    return response


@api_view(['GET'])
@authentication_classes((Authentication, ))
@renderer_classes((JSONRenderer,))
def get_goods_list(request, pk):

    horecama = Horecama.objects.get(pk=pk)
    qset = Goods.objects.filter(horecama=horecama)
    json = GoodsSerializer(qset, many=True, context={'request': request})

    responseData = {
        'data': json.data,
    }
    response = Response(responseData)
    response["Access-Control-Allow-Origin"] = "*"
    return response
