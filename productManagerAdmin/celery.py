import os
from celery import Celery

# Define o settings padrão do Django para o Celery
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "productManagerAdmin.settings.development"
)

app = Celery("productManagerAdmin")

# Lê as configurações do settings.py que começam com CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descobre tarefas automaticamente (tasks.py) em todos os apps instalados
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
