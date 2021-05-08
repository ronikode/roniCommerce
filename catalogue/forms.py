"""
Forms
"""
# Obtiene la informacion de entrada de usuarios.
# Import django libraries -> forms
from decimal import Decimal

from django import forms
from django.core.exceptions import ValidationError

from catalogue.models import ItemModel


# 1.- Form Basic
class ItemBasicForm(forms.Form):
    """

    """
    sku = forms.CharField(
        label="Codigo inventario", max_length=60, help_text="Codigo para inventario producto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el codigo'})
    )
    name = forms.CharField(
        label="Nombre", max_length=145, help_text="Nombre descriptivo del producto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre'})
    )
    pvp = forms.DecimalField(
        label="Precio de venta", decimal_places=2, max_digits=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el pvp'})
    )

    def clean_pvp(self):
        max = 20
        pvp = self.cleaned_data.get('pvp')
        if pvp > Decimal(max):
            raise ValidationError("Error en el campo precio")
        return pvp


# 2.- Model Form
class ItemModelForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ("sku", "name", "pvp")
        # exclude = ("photo")
