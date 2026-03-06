import decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productManager.models import (
    HistoryEntryOutput,
    EntryOutput,
    Product,
    Client,
    Category,
)
from django.contrib.auth.models import User

class HistoryEntryOutputTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(name="TestCategory")
        self.product = Product.objects.create(
            name="TestProduct", inventory_qtd=10, price=decimal.Decimal("149")
        )
        self.product.categories.add(self.category)
        self.client1 = Client.objects.create(name="TestClient", cnpj=123456789)
        self.entry_output = EntryOutput.objects.create(
            product=self.product,
            client=self.client1,
            qtd=5,
            unit_price=decimal.Decimal("99.99"),
            status=1,
            type=1,
        )

        # O EntryOutput acima dispara um signal que cria automaticamente um HistoryEntryOutput.
        # Recuperamos esse objeto em vez de criar outro manualmente, evitando duplicação.
        self.history_entry_output = HistoryEntryOutput.objects.filter(
            entryOutput=self.entry_output
        ).first()

    def test_get_history_entry_outputs_unauthorized(self):
        self.client.force_authenticate(user=None)

        url = reverse("historyentryoutput-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_history_entry_outputs(self):
        url = reverse("historyentryoutput-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_history_entry_output(self):
        url = reverse("historyentryoutput-detail", args=[self.history_entry_output.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(HistoryEntryOutput.objects.count(), 0)
