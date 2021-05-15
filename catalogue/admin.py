from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from catalogue.models import ItemModel, CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ItemModel)
# class ItemModelAdmin(admin.ModelAdmin):
class ItemModelAdmin(ImportExportModelAdmin):
    list_display = ("name", "sku", "category", "pvp", "description")
    search_fields = ["name", "sku"]
    list_filter = ("pvp", "category")
    list_editable = ("pvp",)
    raw_id_fields = ("category",)
    fields = ("name", "photo", "category", "sku", "pvp")
    # list_per_page = 1 (Paginar)
