from rest_framework import serializers
from productManager.models import HistoryEntryOutput
from productManager.serializers import EntryOutputSerializer


class HistoryEntryOutputSerializer(serializers.Serializer):
  entryOutput = EntryOutputSerializer(required=True)
  qtd = serializers.IntegerField(required=False)
  unit_price = serializers.DecimalField(max_digits=4,
                                        decimal_places=2,
                                        required=False)
  status = serializers.IntegerField(required=False)

  class Meta:
    model = HistoryEntryOutput
