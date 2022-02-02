from api.tests.factories import RoomFactory, VehicleFactory, MediaFactory
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):
        print("Creating a test User")
        if User.objects.filter(email='test@email.com').exists():
            print("Test User already exists.")
        else:
            User.objects.create_user(email='test@email.com', name='testuser', password='password')
            print("Test User created.")

        vehicle = VehicleFactory.create()
        MediaFactory(tagged_object=vehicle)
        print(f"Vehicle with name : {vehicle.name} created.")

        room = RoomFactory.create()
        MediaFactory(tagged_object=room)
        print(f"Room with name : {room.title} created.")
