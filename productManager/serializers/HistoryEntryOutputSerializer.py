from rest_framework import serializers
from productManager.models import HistoryEntryOutput
from productManager.serializers import EntryOutputSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class HistoryEntryOutputSerializer(WritableNestedModelSerializer):
  entryOutput = EntryOutputSerializer(required=True)
  qtd = serializers.IntegerField(required=False)
  unit_price = serializers.DecimalField(max_digits=13,
                                        decimal_places=2,
                                        required=False)
  status = serializers.IntegerField(required=False)

  class Meta:
    model = HistoryEntryOutput
    fields = '__all__'
