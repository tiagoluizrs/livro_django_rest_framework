from rest_framework import serializers
from productManager.models import Product
from productManager.serializers import CategorySerializer


class ProductSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=50, required=True)
  image = serializers.ImageField(required=False)
  inventory_qtd = serializers.IntegerField(required=False)
  price = serializers.DecimalField(max_digits=4,
                                   decimal_places=2,
                                   required=False)
  categories = CategorySerializer(many=True, required=False)
  status = serializers.BooleanField(required=False)

  class Meta:
    model = Product
