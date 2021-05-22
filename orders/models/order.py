"""

"""
from django.db import models


class OrderModel(models.Model):
    code = models.CharField(verbose_name="Codigo", help_text="Codigo de la orden", unique=True, max_length=80)
    first_name = models.CharField(verbose_name="Nombres", help_text="Nombres del cliente", max_length=100)
    last_name = models.CharField(verbose_name="Apellidos", help_text="Apellidos del cliente", max_length=100)
    email = models.EmailField(verbose_name="Email")
    dni = models.CharField(verbose_name="No. Identificación", max_length=20)
    city = models.CharField(verbose_name="Ciudad", max_length=80)
    address = models.CharField(verbose_name="Dirección", max_length=200, help_text="Dirección", default="")
    postal_code = models.CharField(verbose_name="Codigo postal", blank=True, default='', max_length=30)
    paid = models.BooleanField(verbose_name="Es pagada", default=False)

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        db_table = "orden"

    def __str__(self) -> str:
        return f"[{self.code}] - {self.first_name} {self.last_name}"

    def to_json(self) -> dict:
        return {
            "code": self.code,
            "dni": self.dni,
            "paid": self.paid
        }
