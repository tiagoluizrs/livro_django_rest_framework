from rest_framework import serializers
from productManager.models import EntryOutput
from productManager.serializers import ClientSerializer, ProductSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class EntryOutputSerializer(WritableNestedModelSerializer):
  product = ProductSerializer(required=False, allow_null=True)
  client = ClientSerializer(required=False, allow_null=True)
  qtd = serializers.IntegerField(required=False)
  unit_price = serializers.DecimalField(max_digits=13,
                                        decimal_places=2,
                                        required=False)
  status = serializers.IntegerField(required=False)
  type = serializers.IntegerField(required=False)

  class Meta:
    model = EntryOutput
    fields = '__all__'
