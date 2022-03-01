from django.core.management.base import BaseCommand
from api.data_loader import seed_users, seed_vehicles, seed_rooms


class Command(BaseCommand):
    help = 'Seed database'

    def add_arguments(self, parser):
        parser.add_argument('seed', nargs='?', type=bool, help='seed rooms and vehicles')

    def handle(self, *args, **options):

        seed_users()
        if options['seed']:
            seed_rooms()
            seed_vehicles()
