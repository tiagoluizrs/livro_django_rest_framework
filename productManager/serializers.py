from rest_framework import serializers
from productManager.models import Category, Product, Client, EntryOutput, HistoryEntryOutput

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    image = serializers.ImageField(required=False, allow_blank=True)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Category

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    image = serializers.ImageField(required=False, blank=True)
    inventory_qtd = serializers.IntegerField(required=False, blank=True)
    price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, blank=True)
    categories = serializers.CategorySerializer(many=True, required=False, allow_blank=True)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Product

class ClientSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_blank=False)
    cnpj = serializers.IntegerField(required=True, allow_blank=False)
    status = serializers.BooleanField(required=False, allow_blank=True)

    class Meta:
        model = Client

class EntryOutputSerializer(serializers.Serializer):
    product = serializers.RelatedField(source='product', required=True, allow_blank=False)
    client = serializers.RelatedField(source='client', required=False, blank=True)
    qtd = serializers.IntegerField(required=False, allow_blank=True)
    unit_price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, allow_blank=True)
    status = serializers.IntegerField(required=False, allow_blank=True)
    type = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
        model = EntryOutput

class HistoryEntryOutputSerializer(serializers.Serializer):
    entryOutput = serializers.RelatedField(source='entryOutput', required=True, allow_blank=False)
    qtd = serializers.IntegerField(required=False, allow_blank=True)
    unit_price = serializers.DecimalField(max_digits=4, decimal_places=2, required=False, allow_blank=True)
    status = serializers.IntegerField(required=False, allow_blank=True)

    class Meta:
        model = HistoryEntryOutput