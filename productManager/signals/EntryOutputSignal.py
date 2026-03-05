from django.db.models.signals import post_save
from django.dispatch import receiver
from productManager.models import EntryOutput, HistoryEntryOutput


@receiver(post_save, sender=EntryOutput)
def create_history_entry_output(sender, instance, created, **kwargs):
    """
    Sinal executado sempre que um EntryOutput é salvo.
    Se for uma criação (created=True), gera o histórico.
    """
    if created:
        HistoryEntryOutput.objects.create(
            entryOutput=instance,
            qtd=instance.qtd,
            unit_price=instance.unit_price,
            status=instance.status,
        )
