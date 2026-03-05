from django.urls import reverse
from rest_framework.test import APITestCase
from productManager.models import Product
from django.contrib.auth.models import User

class ProductViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

    def test_list_products(self):
        Product.objects.create(name="Produto Teste", price=10.0)
        url = reverse("product-list")  # Ajuste conforme o nome da sua rota
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
