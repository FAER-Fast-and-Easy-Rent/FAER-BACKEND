from api.models import Room, Media
from django.contrib.auth import get_user_model

User = get_user_model()


def create_room(data):
    user = User.objects.get(email=data['user'])

    room = Room.objects.create(price=data['price'], description=data['description'], home_type=data['home_type'],
                               room_type=data['room_type'], address=data['address'], owner=user)
    Media.objects.create(content_object=room, file_name=data['images'], url=data['images'], mime_type='image/png')
