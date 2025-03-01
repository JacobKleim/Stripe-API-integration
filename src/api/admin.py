from django.contrib import admin

from api.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
