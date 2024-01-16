from rest_framework import serializers
from productManager.models import Client


class ClientSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=50, required=True)
  cnpj = serializers.IntegerField(required=True)
  status = serializers.BooleanField(required=False)

  class Meta:
    model = Client
