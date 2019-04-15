import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict

from channels import layers
from asgiref.sync import async_to_sync

from core.models import Order, ActiveCourier


def get_json_order(instance):
    return json.dumps(model_to_dict(instance, fields=('user_name', 'user_phone', 'address', 'price')))


@receiver(post_save, sender=Order)
def new_order(sender, instance, **kwargs):
    if not kwargs.pop('created', False):
        return

    channel_layer = layers.get_channel_layer()
    active_couriers = ActiveCourier.objects.all()
    for active_courier in active_couriers:
        if not active_courier.has_order:
            async_to_sync(channel_layer.send)(str(active_courier.channel_name), {'text': get_json_order(instance), 'type': 'send_courier_notify'})
