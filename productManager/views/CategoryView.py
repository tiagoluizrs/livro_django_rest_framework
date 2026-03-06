from rest_framework import generics
from productManager.models import Category

# Novos serializers precisam ser importados aqui
from productManager.serializers import (
    CategorySerializer,
    CategoryListSerializer,
    CategoryUpdateSerializer,
)

# Adicione o import de permissions para validarmos as ações de criação, atualização e deleção de categorias
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from productManager.utils.CustomPagination import CustomPagination

import logging

logger = logging.getLogger("api")


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        logger.info("Rodando o queryset")
        # Customiza o queryset para listar apenas categorias ativas
        return Category.objects.filter(status=True)

    def get_serializer_class(self):
        # Customiza o serializer class dependendo da ação
        if self.request.method == "GET":
            return CategoryListSerializer  # Supondo que você tenha um serializer específico para listagem
        return CategorySerializer

    def get_permissions(self):
        # Customiza as permissões dependendo da ação
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if not obj.status:
            raise NotFound("Esta categoria não está ativa.")
        return obj

    def get_serializer_class(self):
        # Customiza o serializer class dependendo da ação
        if self.request.method in ["PUT", "PATCH"]:
            return CategoryUpdateSerializer  # Supondo que você tenha um serializer específico para atualização
        return CategorySerializer

    def perform_update(self, serializer):
        # Adiciona lógica adicional quando um objeto está sendo atualizado
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        # Adiciona lógica adicional quando um objeto está sendo deletado
        instance.status = False
        instance.save()
