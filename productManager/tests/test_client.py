import decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productManager.models import Client
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ClientTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.client_instance = Client.objects.create(name='TestClient', cnpj=123456789)

    def test_get_clients_unauthorized(self):
        self.client.credentials()

        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_clients(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_client(self):
        url = reverse('client-list')
        data = {'name': 'NewClient', 'cnpj': 987654321}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(id=2).name, 'NewClient')

    def test_delete_client(self):
        url = reverse('client-detail', args=[self.client_instance.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)