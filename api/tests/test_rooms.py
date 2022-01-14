from django.test import TestCase
from rest_framework import status


class RoomsTests(TestCase):

    def test_home_route_of_amenities(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/rooms/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_a_room(self):
        data = {"is_furnished": True, "has_parking": True,
                "has_garden": False, "has_terrace": False,
                "has_attach_bathrooms": True, "floor_no": 1,
                "total_rooms_in_house": 4}
        response = self.client.post('/api/v1/amenties/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data['amenty_id'] = 1
        self.assertJSONEqual(response.content, data)

    def test_create_and_retrieve_amenity_data(self):
        data = {"is_furnished": True, "has_parking": True,
                "has_garden": False, "has_terrace": False,
                "has_attach_bathrooms": True, "floor_no": 1,
                "total_rooms_in_house": 4}
        response1 = self.client.post('/api/v1/amenties/', data)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        id = response1.json()['amenty_id']
        data['amenty_id'] = id
        self.assertJSONEqual(response1.content, data)
        response2 = self.client.get(f'/api/v1/amenties/{id}/')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response2.content, data)
