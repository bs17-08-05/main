from django.urls import path

from .views import order, get_order, change_order

urlpatterns = [
    path('order/', order),
    path('order/<int:id>', get_order),
    path('change_order/<int:id>', change_order)
]
