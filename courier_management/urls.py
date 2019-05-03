from django.urls import path

from .views import index, get_delivered, get_not_delivered, order, delivered

urlpatterns = [
    path('get_active_orders/', index),
    path('get_not_delivered/', get_not_delivered),
    path('get_delivered/', get_delivered),
    path('order/<int:id>/', order),
    path('delivered/<int:id>/', delivered)
]
