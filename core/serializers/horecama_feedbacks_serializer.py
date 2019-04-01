from rest_framework import serializers
from core.models import HorecamaFeedback


class HorecamaFeedbacksSerializer(serializers.ModelSerializer):

    goods_which_was_ordered = serializers.SerializerMethodField()

    class Meta:
        model = HorecamaFeedback
        fields = ('pk', 'user_name', 'goods_which_was_ordered', 'rating', 'time', 'pros', 'cons')

    def get_goods_which_was_ordered(self, feedback: HorecamaFeedback):
        if feedback.order:
            goods = []
            a = feedback.order.goods.get_queryset()
            for i in a:
                goods.append(i.name)
            return goods
        else: return []
