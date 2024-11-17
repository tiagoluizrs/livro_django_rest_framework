import decimal
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from productManager.models import Product, Category
from productManager.serializers import CategorySerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ProductTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(name='TestProduct', inventory_qtd=10, price=decimal.Decimal('149'))
        self.product.categories.add(self.category)
        self.product.save()

    def test_get_products_unauthorized(self):
        self.client.credentials()

        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse('product-list')

        category = CategorySerializer(self.category).data
        data = {'name': 'NewProduct', 'categories': [category], 'price': '199.99', 'inventory_qtd': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(id=2).name, 'NewProduct')

    def test_update_product(self):
        url = reverse('product-detail', args=[self.product.id])
        data = {'name': 'UpdatedProduct'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=self.product.id).name, 'UpdatedProduct')

    def test_delete_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)