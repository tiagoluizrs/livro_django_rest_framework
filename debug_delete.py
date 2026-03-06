import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "productManagerAdmin.settings.settings")
django.setup()

from productManager.models import Category

c = Category.objects.create(name="DebugCat")
print(f"Created category with ID: {c.id}")
print(f"Count before delete: {Category.objects.count()}")
c.delete()
print(f"Count after delete: {Category.objects.count()}")

exists = Category.objects.filter(id=c.id).exists()
print(f"Category exists: {exists}")
