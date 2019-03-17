from rest_framework import serializers
from core.models import Horecama, Goods


class HorecamaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horecama
        fields = ('id', 'name', 'address', 'photo' 'type', 'description')


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = ('id', 'name', 'photo', 'description', 'price')
