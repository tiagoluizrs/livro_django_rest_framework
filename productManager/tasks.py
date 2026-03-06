from celery import shared_task
import time


@shared_task
def enviar_email_boas_vindas(cliente_nome, cliente_cnpj):
    """
    Simula o envio de um email pesado.
    """
    print(f"📧 Iniciando envio de email para {cliente_nome}...")

    # Simulamos uma demora de 5 segundos (ex: conexão SMTP lenta)
    time.sleep(5)

    print(f"✅ Email enviado com sucesso para {cliente_nome} com CNPJ: {cliente_cnpj}!")
    return "Email Enviado"
