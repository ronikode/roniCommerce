"""

"""
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.http import require_POST

from carts.cart import Cart
from carts.forms import CartAddItemForm
from catalogue.models import ItemModel


@require_POST
def cart_add(request, item_id):
    """

    """
    cart = Cart(request)
    item = get_object_or_404(ItemModel, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data  # {"quantity": 1}
        cart.add(
            item=item,
            quantity=data.get("quantity"),
            override_quantity=data.get("override")
        )
        messages.success(request, "Item agregado exitosamente!")
    return redirect("")  # Redirect cartDetail


@require_POST
def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(ItemModel, id=item_id)
    cart.remove(item=item)
    messages.success(request, "Item removido exitosamente del carrito!")
    return redirect("")  # Redirect cartDetail
