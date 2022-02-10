from django.core.management.base import BaseCommand
from api.data_loader import seed_users, seed_vehicles, seed_rooms


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):

        seed_users()
        seed_rooms()
        seed_vehicles()
