from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from apps.users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


data = {"username": "testcase", "password": "some_strong_psw"}

class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = User.objects.create_user(**self.user_data)
        self.token = RefreshToken.for_user(self.user)
        self.access_token = str(self.token.access_token)

    def test_registration(self):
        response = self.client.post("/api/v1/signup/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('token_obtain_pair')
        data = {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
 
    def test_access_protected_view(self):
        url = '/api/v1/posts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
