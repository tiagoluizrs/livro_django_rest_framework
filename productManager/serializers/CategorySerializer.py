from rest_framework import serializers
from productManager.models import Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    image = serializers.ImageField(required=False, allow_blank=True)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Category