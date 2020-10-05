from django.test import TestCase
from rest_framework.test import APIClient


class AuthTest(TestCase):

    fixtures = ['swap_analysis/fixtures/authentication.json', ]

    def setUp(self):
        # attendant = User.objects.get(username='attendant')
        # token = Token.objects.get_or_create(user=attendant)
        # import pdb
        # pdb.set_trace()
        # self.user = token.user
        self.client = APIClient()
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_successful_login(self):
        user = {'email': 'attendant@ampersand.solar',
                'password': 'Password123'}
        response = self.client.post(
            '/login', data=user)

        self.assertIsNotNone(response.data['token'])
        self.assertEqual(user['email'], response.data['email'])

    def test_invalid_email(self):
        user = {'email': 'attendant@amp.solar',
                'password': 'Password123'}
        response = self.client.post(
            '/login', data=user)
        self.assertEqual('Invalid email or password', response.data['detail'])

    def test_invalid_password(self):
        user = {'email': 'attendant@ampersand.solar',
                'password': 'invalidPass'}
        response = self.client.post(
            '/login', data=user)
        self.assertEqual('Invalid email or password', response.data['detail'])
