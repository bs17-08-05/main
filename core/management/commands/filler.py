from django.core.management.base import BaseCommand
from core.models import Horecama, Goods, HorecamaFeedback, Order, GoodsQuantityOrder


class Command(BaseCommand):
    help = 'The DB Filler'

    def handle(self, *args, **options):

        restaurant = Horecama(name='108', address='Улица Универститетская блабла', type='R', description='Блабла')
        restaurant.save()

        restaurant = Horecama(name='Pyatorochka', address='Улица Универститетская блабла', type='M', description='Блабла')
        restaurant.save()

        restaurant = Horecama(name='Bechetle', address='Улица Универститетская блабла', type='M', description='Блабла')
        restaurant.save()

        g1 = Goods(name="Ananas", description="", price="20", horecama=restaurant)
        g1.save()

        g2 = Goods(name="Pivas", description="", price="20", horecama=restaurant)
        g2.save()

        g3 = Goods(name="Vodka", description="", price="200", horecama=restaurant)
        g3.save()


        order = Order(user_name='Vladimir Kekovich', user_phone='88005553535', address='Улица универская блабла', price=200)
        order.save()
        mtm = GoodsQuantityOrder(quantity=10, order=order, goods=g1)
        mtm.save()
        mtm = GoodsQuantityOrder(quantity=10, order=order, goods=g2)
        mtm.save()
        mtm = GoodsQuantityOrder(quantity=10, order=order, goods=g3)
        mtm.save()


        feedback = HorecamaFeedback(user_name='Vladimir Kekovich', horecama=restaurant, rating=4, order=order)
        feedback.save()

        feedback = HorecamaFeedback(user_name='Ivan Kekovich', horecama=restaurant, rating=5)
        feedback.save()

        feedback = HorecamaFeedback(user_name='Sashok Kekovich', horecama=restaurant, rating=1)
        feedback.save()



        return restaurant.name
