import decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productManager.models import HistoryEntryOutput, EntryOutput, Product, Client, Category
from productManager.serializers import EntryOutputSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class HistoryEntryOutputTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(name='TestProduct', inventory_qtd=10, price=decimal.Decimal('149'))
        self.product.categories.add(self.category)
        self.client1 = Client.objects.create(name='TestClient', cnpj=123456789)
        self.entry_output = EntryOutput.objects.create(product=self.product, client=self.client1, qtd=5, unit_price=decimal.Decimal('99.99'), status=1, type=1)

        self.history_entry_output = HistoryEntryOutput.objects.create(entryOutput=self.entry_output, qtd=5, unit_price=decimal.Decimal('99.99'), status=1)

    def test_get_history_entry_outputs_unauthorized(self):
        self.client.credentials()

        url = reverse('historyentryoutput-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_history_entry_outputs(self):
        url = reverse('historyentryoutput-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_history_entry_output(self):
        url = reverse('historyentryoutput-list')
        data = {
            'entryOutput': EntryOutputSerializer(self.entry_output).data,
            'qtd': 10,
            'unit_price': '199.99',
            'status': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HistoryEntryOutput.objects.count(), 2)
        self.assertEqual(HistoryEntryOutput.objects.get(id=2).qtd, 10)

    def test_delete_history_entry_output(self):
        url = reverse('historyentryoutput-detail', args=[self.history_entry_output.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HistoryEntryOutput.objects.count(), 0)