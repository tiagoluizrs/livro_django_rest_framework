from rest_framework import serializers
from productManager.models import Category
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CategorySerializer(WritableNestedModelSerializer):
  name = serializers.CharField(max_length=50, required=True)
  image = serializers.ImageField(required=False)
  status = serializers.BooleanField(required=False)

  class Meta:
    model = Category
    fields = '__all__'
