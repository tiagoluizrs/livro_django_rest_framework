from rest_framework import viewsets
from productManager.models import EntryOutput
from productManager.serializers import EntryOutputSerializer
from rest_framework import permissions


class EntryOutputView(viewsets.ModelViewSet):
  queryset = EntryOutput.objects.all()
  serializer_class = EntryOutputSerializer
  permission_classes = [permissions.IsAuthenticated]
  search_fields = ['product__name']
