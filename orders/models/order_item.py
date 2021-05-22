"""

"""
from django.db import models


class OrderItemModel(models.Model):
    order = models.ForeignKey("orders.OrderModel", related_name="items", on_delete=models.CASCADE)
    item = models.ForeignKey("catalogue.ItemModel", related_name="order_items",
                             on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"OrderItem: {self.id} - {self.item}"

    class Meta:
        verbose_name = "OrderItem"
        db_table = "order_item"

    def get_subtotal(self):
        return self.quantity * self.price
