from channels.routing import URLRouter
from django.urls import path
from .ws_view import CourierConsumer


channel_routing = URLRouter([
    path('api/ws/courier/notification', CourierConsumer),
])
