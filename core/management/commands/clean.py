from django.core.management.base import BaseCommand
from core.models import Horecama, Goods

class Command(BaseCommand):
    help = 'The DB Cleaner'

    def handle(self, *args, **options):

        Horecama.objects.all().delete()
        Goods.objects.all().delete()

        return "Cleaned"
