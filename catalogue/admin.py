from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from catalogue.models import ItemModel


@admin.register(ItemModel)
# class ItemModelAdmin(admin.ModelAdmin):
class ItemModelAdmin(ImportExportModelAdmin):
    list_display = ("name", "sku", "pvp", "description")
    search_fields = ["name", "sku"]
    list_filter = ("pvp",)
    list_editable = ("pvp",)
    fields = ("name", "photo", "sku", "pvp")
    # list_per_page = 1 (Paginar)
