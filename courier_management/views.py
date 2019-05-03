from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes, api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.authentication import Authentication
from core.models import Order, Courier
from core.serializers import order_serializer


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
@authentication_classes((Authentication, ))
def index(request):
    if not request.user:
        return Response({'Jopa': 'Jopa'}, status=403)
    active_orders = Order.objects.filter(active=True, delivered=False, finished=False).order_by('-time')
    orders = [order_serializer(order) for order in active_orders]
    return Response(orders)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
@authentication_classes((Authentication, ))
def get_not_delivered(request):
    if not request.user:
        return Response({'Jopa': 'Jopa'}, status=403)
    courier = Courier.objects.filter(user=request.user.id).first()
    orders = courier.orders.filter(active=False, delivered=False, finished=False).order_by('-time')
    orders = [order_serializer(order) for order in orders]
    return Response(orders)


@api_view(['GET'])
@renderer_classes((JSONRenderer, ))
@authentication_classes((Authentication, ))
def get_delivered(request):
    if not request.user:
        return Response({'Jopa': 'Jopa'}, status=403)
    courier = Courier.objects.filter(user=request.user.id).first()
    orders = courier.orders.filter(active=False, delivered=True, finished=True)
    orders = [order_serializer(order) for order in orders]
    return Response(orders)


@api_view(['POST'])
@renderer_classes((JSONRenderer, ))
@authentication_classes((Authentication, ))
def order(request, id):
    if not request.user:
        return Response({'Jopa': 'Jopa'}, status=403)
    order = get_object_or_404(Order, id=id)
    order.active = False
    order.save()
    courier = Courier.objects.filter(user=request.user.id).first()
    courier.orders.add(order)
    return Response({'nice': 'nice'})


@api_view(['POST'])
@renderer_classes((JSONRenderer, ))
@authentication_classes((Authentication, ))
def delivered(request, id):
    if not request.user:
        return Response({'Jopa': 'Jopa'}, status=403)
    order = get_object_or_404(Order, id=id)
    order.finished = True
    order.delivered = True
    order.save()
    return Response({'nice': 'nice'})
