from django.db.models.signals import post_save
from django.dispatch import receiver
from productManager.models import Client
from productManager.tasks import enviar_email_boas_vindas


@receiver(post_save, sender=Client)
def notificar_novo_cliente(sender, instance, created, **kwargs):
    if created:
        # .delay() é o segredo! Ele envia a tarefa para a fila do Celery
        # e o código continua IMEDIATAMENTE, sem esperar os 5 segundos.
        enviar_email_boas_vindas.delay(instance.name, instance.cnpj)
