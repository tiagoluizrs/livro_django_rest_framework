from rest_framework import viewsets
from productManager.models import Product
from productManager.serializers import ProductSerializer
from rest_framework import permissions
from productManager.utils.CustomPagination import CustomPagination


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["name"]
    pagination_class = CustomPagination
