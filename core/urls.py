from django.urls import path
from core.views import get_horecama_list
from core.views import get_goods_list
from core.views import order, get_order, change_order

urlpatterns = [
    path('horecama/', get_horecama_list),
    path('goods/<int:pk>/', get_goods_list),
    path('order/', order),
    path('order/<int:id>', get_order),
    path('change_order/<int:id>', change_order)
]
