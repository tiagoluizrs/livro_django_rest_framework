from rest_framework import serializers
from productManager.models import EntryOutput

class EntryOutputSerializer(serializers.Serializer):
    product = serializers.RelatedField(source='product', required=True, allow_blank=False)
    client = serializers.RelatedField(source='client', required=False, blank=True)
    qtd = serializers.IntegerField(required=False, allow_blank=True)
    unit_price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, allow_blank=True)
    status = serializers.IntegerField(required=False, allow_blank=True)
    type = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
        model = EntryOutput