from django.test import TestCase
from productManager.serializers import ProductSerializer
from productManager.models import Product

class ProductSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        product = Product.objects.create(name="Produto Teste", price=10.0)
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data["name"], "Produto Teste")
        self.assertEqual(serializer.data["price"], "10.00")
