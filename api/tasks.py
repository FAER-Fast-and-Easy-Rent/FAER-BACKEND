from django.db import transaction
from api.models import Room, Media
from .utils import upload_to_storage
from django.contrib.auth import get_user_model

User = get_user_model()


def create_room(data):
    if User.objects.filter(email=data['user']).exists():
        with transaction.atomic():
            image = upload_to_storage(file_path=data['images'])
            print(image)
            user = User.objects.get(email=data['user'])

            room = Room.objects.create(price=data['price'], title=data['title'], description=data['description'],
                                       home_type=data['home_type'], room_type=data['room_type'],
                                       address=data['address'], owner=user)
            Media.objects.create(content_object=room,
                                 file_name=data['images'], url=data['images'], mime_type='image/png')

            print("Room created successfuly.")
    else:
        print('User Not Found. Data not created')
