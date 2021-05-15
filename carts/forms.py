from django import forms

ITEM_QUANTITY_CHOICES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class CartAddItemForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=ITEM_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
