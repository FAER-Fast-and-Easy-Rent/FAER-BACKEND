from django.test import TestCase
from rest_framework import status


class AmenitiesTests(TestCase):

    def test_home_route_of_amenities(self):
        # Issue a GET request.
        response = self.client.get('/api/v1/amenties/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the content of the response contains messgae.
        self.assertEqual(response.content, b'[]')

    def test_create_a_amenity(self):
        data = {"is_furnished": True, "has_parking": True,
                "has_garden": False, "has_terrace": False,
                "has_attach_bathrooms": True, "floor_no": 1,
                "total_rooms_in_house": 4}
        response = self.client.post('/api/v1/amenties/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data['amenty_id'] = 1
        self.assertJSONEqual(response.content, data)
