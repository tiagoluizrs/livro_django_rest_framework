from rest_framework import serializers
from productManager.models import Client
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ClientSerializer(WritableNestedModelSerializer):
  name = serializers.CharField(max_length=50, required=True)
  cnpj = serializers.IntegerField(required=True)
  status = serializers.BooleanField(required=False)

  class Meta:
    model = Client
    fields = '__all__'
