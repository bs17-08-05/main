from django.urls import path
from core.views import get_horecama_list
from core.views import get_goods_list


urlpatterns = [
    path('horecama/', get_horecama_list),
    path('goods/<int:pk>/', get_goods_list),
]