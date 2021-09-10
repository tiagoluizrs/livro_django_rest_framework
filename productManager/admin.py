from django.contrib import admin
from productManager.models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'getAllCategories')

    def getAllCategories(self, obj):
        return [o.name for o in obj.categories.all()]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
admin.site.register(EntryOutput)
admin.site.register(HistoryEntryOutput)
