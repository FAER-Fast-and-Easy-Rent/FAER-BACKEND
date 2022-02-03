from django.db import transaction
from .utils import upload_to_storage
from api.models import Room, Media, Vehicle
from django.contrib.auth import get_user_model

User = get_user_model()


def create_room(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            image = upload_to_storage(file_path=data['image'])
            print(image)
            user = User.objects.get(email=data['user'])

            room = Room.objects.create(price=data['price'], title=data['title'], description=data['description'],
                                       home_type=data['home_type'], room_type=data['room_type'],
                                       address=data['address'], owner=user)
            Media.objects.create(content_object=room,
                                 file_name=data['image'], url=data['image'], mime_type='image/png')

            print("Room created successfuly.")
    else:
        print('User Not Found. Data not created')


def create_vehicle(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            image = upload_to_storage(file_path=data['image'])
            print(image)
            user = User.objects.get(email=data['user'])

            vehicle = Vehicle.objects.create(name=data['name'], price=data['price'], description=data['description'],
                                             capacity=data['capacity'], vehicle_type=data['vehicle_type'],
                                             brand=data['brand'], model=data['model'], owner=user)
            Media.objects.create(content_object=vehicle,
                                 file_name=data['image'], url=data['image'], mime_type='image/png')

            print("Vehicle created successfuly.")
    else:
        print('User Not Found. Data not created')
