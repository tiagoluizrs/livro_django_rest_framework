from rest_framework import serializers
from productManager.models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    image = serializers.ImageField(required=False, blank=True)
    inventory_qtd = serializers.IntegerField(required=False, blank=True)
    price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, blank=True)
    categories = serializers.CategorySerializer(many=True, required=False, allow_blank=True)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Product