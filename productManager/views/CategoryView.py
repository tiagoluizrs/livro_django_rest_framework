from rest_framework import viewsets
from productManager.models import Category
from productManager.serializers import CategorySerializer
from rest_framework import permissions


class CategoryView(viewsets.ModelViewSet):
    """
    list:
    Retorna todas as categorias cadastradas.

    create:
    Cria uma nova categoria.

    retrieve:
    Retorna os detalhes de uma categoria específica.

    update:
    Atualiza todos os dados de uma categoria.

    partial_update:
    Atualiza parcialmente os dados de uma categoria.

    destroy:
    Remove uma categoria do sistema.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ["name"]
