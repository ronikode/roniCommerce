from django import forms

from orders.models import OrderModel


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = "__all__"
