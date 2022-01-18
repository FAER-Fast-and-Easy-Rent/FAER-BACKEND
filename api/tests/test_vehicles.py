from api.models import Vehicle
from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class VehiclesTests(TestCase):

    file_name = 'media/hyundai-kona.jpg'

    data = {"name": "Hyundai Konka", "price": 5000, "description": "This is car.","capacity":6, "vehicle_type": "Car",
            "brand": "Hyundai","model": "SUV", "images": open(file_name, "rb")}

    def test_home_route_of_rooms(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/vehicles/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_and_retrieve_vehicle_data(self):
        user = User.objects.create_user(email='normal@user.com', name='normal', password='password@123')
        response = self.client.post('/api/v1/token/', {'email': user.email, 'password': 'password@123'})
        header = {'HTTP_AUTHORIZATION': f'Bearer {response.data["access"]}'}
        response = self.client.post('/api/v1/vehicles/', self.data, **header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data['message'], 'OK')
        # self.assertEqual(response.data['data']['title'], self.data['title'])
        # self.assertEqual(response.data['data']['price'], self.data['price'])

        # data = self.data
        # room = Room.objects.create(price=data['price'], title=data['title'],
        #                            description=data['description'], home_type=data['home_type'],
        #                            room_type=data['room_type'], address=data['address'], owner=user)
        # response = self.client.get('/api/v1/rooms/')
        # self.assertEqual(response.data[0]['title'], room.title)
        # self.assertEqual(response.data[0]['price'], room.price)

        # # unique room with title validation test
        # response = self.client.post('/api/v1/rooms/', self.data, **header)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(response.data['title'], ["This field must be unique."])
