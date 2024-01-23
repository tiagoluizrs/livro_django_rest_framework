from rest_framework import viewsets
from productManager.models import Category
from productManager.serializers import CategorySerializer
from rest_framework import permissions


class CategoryView(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated]
  search_fields = ['name']
