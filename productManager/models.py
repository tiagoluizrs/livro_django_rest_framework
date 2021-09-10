from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    image = models.ImageField(null=True, blank=True, verbose_name='Imagem')
    inventory_qtd = models.IntegerField(default=0, verbose_name='Quantidade em estoque')
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Valor')
    categories = models.ManyToManyField(Category, related_name='product_category', verbose_name='Categorias')
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Client(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    cnpj = models.IntegerField(null=False, blank=False)
    status = models.BooleanField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class EntryOutput(models.Model):
    product = models.ForeignKey(Product, related_name='entryOutput_product', on_delete=models.CASCADE, verbose_name='Produto')
    client = models.ForeignKey(Client, related_name='entry_client', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cliente')
    qtd = models.IntegerField(default=0, verbose_name='Quantitdade')
    unit_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Preço unitário')
    status = models.IntegerField(default=1, choices=(
                                                        (1, 'SUCCESS'),
                                                        (2, 'BROKED'),
                                                        (3, 'RETURNED')
                                                    ), verbose_name='Estado atual da entrada/saída')
    type = models.IntegerField(default=1, choices=(
                                                        (1, 'entry'),
                                                        (2, 'output')
                                                  ), verbose_name='Tipo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = "Entrada e/ou Saída"
        verbose_name_plural = "Estadas e/ou Saídas"

class HistoryEntryOutput(models.Model):
    entryOutput = models.ForeignKey(EntryOutput, related_name='entryOutputHistory_entryOutput', on_delete=models.CASCADE, verbose_name='Entrada e/ou Saída')
    qtd = models.IntegerField(default=0, verbose_name='Quantitdade')
    unit_price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Preço unitário')
    status = models.IntegerField(default=1, choices=(
        (1, 'SUCCESS'),
        (2, 'BROKED'),
        (3, 'RETURNED')
    ), verbose_name='Estado atual da entrada/saída')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = "Histórico de Entrada e/ou Saída"
        verbose_name_plural = "Históricos de Estadas e/ou Saídas"
