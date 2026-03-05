from django.apps import AppConfig


class ProductmanagerConfig(AppConfig):
    name = "productManager"

    def ready(self):
        import productManager.signals
