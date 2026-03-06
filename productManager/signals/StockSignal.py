from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from productManager.models import Product


@receiver(post_save, sender=Product)
def broadcast_stock_update(sender, instance, created, **kwargs):
    """
    Envia uma mensagem para o grupo 'global_stock' sempre que um produto é salvo.
    """
    if not created:  # Só queremos atualizações, não criações (opcional)
        channel_layer = get_channel_layer()

        # O group_send é assíncrono, então usamos async_to_sync para chamar dentro do sinal síncrono
        async_to_sync(channel_layer.group_send)(
            "global_stock",
            {
                "type": "stock_update",  # Nome do método no Consumer
                "message": {
                    "id": instance.id,
                    "name": instance.name,
                    "new_stock": instance.inventory_qtd,
                },
            },
        )
