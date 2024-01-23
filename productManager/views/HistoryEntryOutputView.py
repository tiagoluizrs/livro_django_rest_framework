from rest_framework import viewsets
from productManager.models import HistoryEntryOutput
from productManager.serializers import HistoryEntryOutputSerializer
from rest_framework import permissions


class HistoryEntryOutputView(viewsets.ModelViewSet):
  queryset = HistoryEntryOutput.objects.all()
  serializer_class = HistoryEntryOutputSerializer
  permission_classes = [permissions.IsAuthenticated]
  search_fields = ['entryOutput__product__name']
