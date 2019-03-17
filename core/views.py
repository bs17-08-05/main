from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.models import Horecama, Goods
from django.core import serializers
from core.serializers.serializers import HorecamaSerializer, GoodsSerializer

# assuming obj is a model instance

# Horecama catalog
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_horecama_list(request):

    qset = Horecama.objects.values('name', 'address', 'photo', 'type', 'description')
    json = HorecamaSerializer(qset, many=True)
    size = len(qset)

    responseData = {
        'data': json.data,
        'size': size,
    }

    return Response(responseData)

# Goods catalog
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_goods_list(request, pk):

    horecama = Horecama.objects.get(pk=pk)
    qset = Goods.objects.filter(horecama=horecama)
    json = GoodsSerializer(qset, many=True)

    responseData = {
        'data': json.data,
    }

    return Response(responseData)
