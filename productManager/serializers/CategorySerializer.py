from rest_framework import serializers
from productManager.models import Category


class CategorySerializer(serializers.Serializer):
  name = serializers.CharField(max_length=50, required=True)
  image = serializers.ImageField(required=False)
  status = serializers.BooleanField(required=False)

  class Meta:
    model = Category
