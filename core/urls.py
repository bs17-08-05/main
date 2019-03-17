from django.urls import path

from .views import order, get_order, change_order, delete_order

urlpatterns = [
    path('order/', order),
    path('order/<int:id>', get_order),
    path('change_order/<int:id>', change_order),
    path('delete_order/<int:id>', delete_order)
]
