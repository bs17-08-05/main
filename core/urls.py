from django.urls import path

from core.views import order, get_order, change_order, delete_order, get_horecama_list, get_goods_list, get_horecama_feedbacks


urlpatterns = [
    path('horecama/', get_horecama_list),
    path('horecama_feedbacks/<int:pk>/', get_horecama_feedbacks),
    path('goods/<int:pk>/', get_goods_list),
    path('order/', order),
    path('order/<int:id>', get_order),
    path('change_order/<int:id>', change_order),
    path('delete_order/<int:id>', delete_order)
]
