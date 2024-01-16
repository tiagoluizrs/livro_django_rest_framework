from rest_framework import serializers
from productManager.models import HistoryEntryOutput

class HistoryEntryOutputSerializer(serializers.Serializer):
    entryOutput = serializers.RelatedField(source='entryOutput', required=True, allow_blank=False)
    qtd = serializers.IntegerField(required=False, allow_blank=True)
    unit_price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, allow_blank=True)
    status = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
        model = HistoryEntryOutput