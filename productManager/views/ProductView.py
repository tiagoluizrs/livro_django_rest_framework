from rest_framework import viewsets, permissions
from productManager.models import Product
from productManager.serializers import ProductSerializer

# Importamos o decorador
from drf_spectacular.utils import extend_schema


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["name"]

    # Sobrescrevemos o método 'list' apenas para decorar com documentação
    @extend_schema(
        summary="Listar Produtos",
        description="Retorna uma lista paginada de todos os produtos ativos no sistema. Você pode filtrar pelo nome.",
        responses={200: ProductSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Sobrescrevemos o 'create' para explicar melhor
    @extend_schema(
        summary="Criar Produto",
        description="Cria um novo produto. O preço deve ser maior que zero.",
        responses={201: ProductSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
