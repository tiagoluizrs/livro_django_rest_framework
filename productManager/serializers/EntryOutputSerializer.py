from rest_framework import serializers
from productManager.models import EntryOutput
from productManager.serializers import ClientSerializer, ProductSerializer


class EntryOutputSerializer(serializers.Serializer):
  product = ProductSerializer()
  client = ClientSerializer()
  qtd = serializers.IntegerField(required=False)
  unit_price = serializers.DecimalField(max_digits=4,
                                        decimal_places=2,
                                        required=False)
  status = serializers.IntegerField(required=False)
  type = serializers.IntegerField(required=False)

  class Meta:
    model = EntryOutput
