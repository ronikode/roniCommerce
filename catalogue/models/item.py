"""

"""

# Import django db libraries.
from decimal import Decimal

from django.db import models


class ItemModel(models.Model):
    # id (primary key unique autoincrement) 1, 2, 9
    category = models.ForeignKey(
        'catalogue.CategoryModel', verbose_name="Categoría",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='items'
    )  # Uno a muchos
    name = models.CharField(verbose_name="Nombre", max_length=150,
                            help_text="Nombre del item")  # varchar en bd o string.
    sku = models.CharField(max_length=20, verbose_name="Codigo", help_text="Codigo del producto")
    description = models.TextField(
        verbose_name="Descripcion", help_text="Descripcion del item",
        blank=True, default=""
    )
    pvp = models.DecimalField(
        decimal_places=3, max_digits=8, verbose_name="Precio de venta",
        help_text="Precio de venta del item."
    )
    photo = models.ImageField(
        verbose_name="Imagen", help_text="Foto principal del producto", null=True, blank=True,
        upload_to='item'
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "item"

    def __str__(self):
        return f"[{self.sku}] - {self.name}"

    def percentage_discount(self):
        return Decimal(0.2) * self.pvp
