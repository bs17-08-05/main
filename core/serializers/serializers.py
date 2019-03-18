from rest_framework import serializers
from core.models import Horecama, Goods


class HorecamaSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Horecama
        fields = ('pk', 'name', 'address', 'photo_url', 'type', 'description')
    
    def get_photo_url(self, horecama):
        request = self.context.get('request')
        photo_url = horecama.photo.url
        return request.build_absolute_uri(photo_url)


class GoodsSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Goods
        fields = ('id', 'name', 'photo_url', 'description', 'price')

    def get_photo_url(self, goods):
        request = self.context.get('request')
        photo_url = goods.photo.url
        return request.build_absolute_uri(photo_url)
