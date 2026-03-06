import csv
from django.http import StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework import permissions
from productManager.models import Product

# Atualizamos o import para refletir o novo caminho
from productManager.utils.echo import Echo


class ProductExportCSVView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Streams a large CSV file of all products."""

        # 1. Definimos o gerador de linhas
        def rows_iterator():
            yield ["ID", "Nome", "Preço", "Categoria", "Estoque"]

            # Usamos prefetch_related para otimizar as consultas N+1
            # Como iterator() não suporta prefetch_related diretamente, vamos paginar ou usar sem iterator
            # se a tabela for gigante, mas para CSV simples, queryset normal com prefetch é mais seguro.

            # Se a tabela for MUITO grande, iterar sem prefetch no 'categories' vai gerar N+1 queries.
            # Alternativa: usar ValuesList ou Values se não precisar de métodos do modelo.

            queryset = Product.objects.all().prefetch_related("categories")

            for product in queryset:
                categories_str = ", ".join(
                    [cat.name for cat in product.categories.all()]
                )
                yield [
                    product.id,
                    product.name,
                    product.price,
                    categories_str,
                    product.inventory_qtd,
                ]

        # 2. Inicializamos o buffer falso e o escritor CSV
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)

        # 3. Gerador final que converte lista -> linha CSV string
        response_generator = (writer.writerow(row) for row in rows_iterator())

        # 4. Retornamos a resposta streaming
        response = StreamingHttpResponse(response_generator, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="produtos.csv"'
        return response
