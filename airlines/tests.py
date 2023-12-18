from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Testplane

class AirplaneListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_airplane(self):
        url = reverse('airplane-list-create')
        data = {'plane_id': 1, 'passenger_capacity': 100}
        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Testplane.objects.count(), 1)
        self.assertEqual(Testplane.objects.get().id, 1)
#Allow for input of 10 airplanes with user defined id and passenger assumptions
    def test_allow_ten_airplanes(self):
        url = reverse('airplane-list-create')
        for i in range(11):
            data = {'plane_id': 1, 'passenger_capacity': 100}
            response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Add more test methods as needed
