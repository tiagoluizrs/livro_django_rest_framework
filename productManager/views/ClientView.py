from rest_framework import viewsets
from productManager.models import Client
from productManager.serializers import ClientSerializer
from rest_framework import permissions


class ClientView(viewsets.ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  permission_classes = [permissions.IsAuthenticated]
  search_fields = ['name']
