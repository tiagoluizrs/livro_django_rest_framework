from rest_framework import serializers
from productManager.models import Client

class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    cnpj = serializers.IntegerField(required=True, allow_blank=False)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Client