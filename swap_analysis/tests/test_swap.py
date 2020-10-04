from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from datetime import datetime
from swap_analysis.apps.authentication.models import User


class SwapTest(TestCase):

    fixtures = ['swap_analysis/fixtures/authentication.json',
                'swap_analysis/fixtures/battery.json',
                'swap_analysis/fixtures/station.json',
                'swap_analysis/fixtures/attendant.json',
                'swap_analysis/fixtures/driver.json',
                'swap_analysis/fixtures/motor.json',
                'swap_analysis/fixtures/battery.json',
                'swap_analysis/fixtures/station.json',
                'swap_analysis/fixtures/swap.json'
                ]

    def setUp(self):
        attendant = User.objects.get(username='attendant')
        token = Token.objects.get_or_create(user=attendant)[0]
        self.data = {
            "battery_in": "0093b3af-461d-49c0-8779-8cf1df011055",
            "battery_out": "0df55090-29e4-4f6c-a35e-1e46e7502727",
            "driver": "a1fc6a64-218b-4385-8bc9-02bc36ac344e",
            "station": "243efd09-fef4-449b-a037-d01f9b39966a",
            "attendant": "3ef6debf-86af-4e12-8e82-6bc800f61d3b",
            "driven_distance": 64,
            "out_state_of_charge": 100,
            "in_state_of_charge": 20,
            "used_energy": 55,
        }

        self.user = token.user
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_swap(self):

        response = self.client.post(
            '/swaps', data=self.data)
        self.assertIsNotNone(response.data)

        self.assertEqual(self.data['battery_in'],
                         str(response.data['battery_in']))
        self.assertEqual(self.data['battery_out'],
                         str(response.data['battery_out']))

    def test_invalid_data(self):
        self.data['battery_in'] = 'fwefwewe'
        response = self.client.post(
            '/swaps', data=self.data)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('fwefwewe' in str(response.data['battery_in'][0]))
        self.assertTrue('is not a valid UUID' in str(
            response.data['battery_in'][0]))

    def test_total_energy_empty(self):

        response = self.client.get(
            '/total_energy')

        self.assertEqual(str(datetime.now().date()), response.data['date'])
        self.assertEqual(0, response.data['used_energy'])

    def test_total_energy_after_swap(self):
        self.client.post(
            '/swaps', data=self.data)
        response = self.client.get(
            '/total_energy')

        self.assertEqual(str(datetime.now().date()), response.data['date'])
        self.assertEqual(self.data['used_energy'],
                         response.data['used_energy'])

    def test_total_distance(self):

        response = self.client.get(
            '/distance_driven')

        self.assertEqual(str(datetime.now().date()), response.data['date'])
        self.assertEqual(0, response.data['driven_distance'])

    def test_total_distance_after_swap(self):
        self.client.post(
            '/swaps', data=self.data)
        response = self.client.get(
            '/distance_driven')

        self.assertEqual(str(datetime.now().date()), response.data['date'])
        self.assertEqual(self.data['driven_distance'],
                         response.data['driven_distance'])

    def test_get_swaps(self):

        response = self.client.get(
            '/swaps')
        self.assertTrue(len(response.data) > 0)
