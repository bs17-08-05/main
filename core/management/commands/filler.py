from django.core.management.base import BaseCommand
from core.models import Horecama, Goods

class Command(BaseCommand):
    help = 'The DB Filler'

    def handle(self, *args, **options):

        restaurant = Horecama(name='108', address='Улица Универститетская блабла', type='R', description='Блабла')
        restaurant.save()

        goods = Goods(name="Ananas", description="", price="20", horecama=restaurant)
        goods.save()

        goods = Goods(name="Pivas", description="", price="20", horecama=restaurant)
        goods.save()

        goods = Goods(name="Vodka", description="", price="200", horecama=restaurant)
        goods.save()

        return restaurant.name
