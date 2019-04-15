import json
from channels.generic.websocket import WebsocketConsumer

from .models import ActiveCourier


class CourierConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        active_courier = ActiveCourier(channel_name=self.channel_name, has_order=False)
        active_courier.save()

    def disconnect(self, close_code):
        ActiveCourier.objects.get(channel_name=self.channel_name).delete()

    def receive(self, text_data=None, bytes_data=None):
        pass

    def send_courier_notify(self, event):
        self.send(text_data=event['text'])
