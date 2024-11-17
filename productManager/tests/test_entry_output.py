import decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productManager.models import EntryOutput, Product, Client, Category
from productManager.serializers import ProductSerializer, ClientSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class EntryOutputTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(name='TestProduct', inventory_qtd=10, price=decimal.Decimal('149'))
        self.product.categories.add(self.category)
        self.client_instance = Client.objects.create(name='TestClient', cnpj=123456789)
        self.entry_output = EntryOutput.objects.create(product=self.product, client=self.client_instance, qtd=5, unit_price=decimal.Decimal('199.99'), status=1, type=1)

    def test_get_entry_outputs_unauthorized(self):
        self.client.credentials()

        url = reverse('entryoutput-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_entry_outputs(self):
        url = reverse('entryoutput-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_entry_output(self):
        url = reverse('entryoutput-list')
        data = {'product': ProductSerializer(self.product).data, 'client': ClientSerializer(self.client_instance).data, 'qtd': 10, 'unit_price': '199.99', 'status': 1, 'type': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EntryOutput.objects.count(), 2)

    def test_update_entry_output(self):
        url = reverse('entryoutput-detail', args=[self.entry_output.id])
        data = {'qtd': 15}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(EntryOutput.objects.get(id=self.entry_output.id).qtd, 15)

    def test_delete_entry_output(self):
        url = reverse('entryoutput-detail', args=[self.entry_output.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EntryOutput.objects.count(), 0)