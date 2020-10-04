from django.test import TestCase
from rest_framework.test import APIClient


class AuthTest(TestCase):
    # FIXTURE_DIRS = ('/swap_analysis/fixtures/',)

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
        user = {'username': 'attendant@ampersand.solar',
                'password': 'Password123'}
        response = self.client.post(
            '/login', data=user)
        self.assertIsNotNone(response.data['token'])
        self.assertEqual(user['username'], response.data['email'])
