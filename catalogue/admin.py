from django.contrib import admin

from catalogue.models import ItemModel


@admin.register(ItemModel)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "pvp", "description")
    search_fields = ["name", "sku"]
    list_filter = ("pvp",)
    list_editable = ("pvp",)
    # list_per_page = 1 (Paginar)
