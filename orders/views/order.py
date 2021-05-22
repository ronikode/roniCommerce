""""""
from django.shortcuts import render

from carts.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItemModel


def order_create(request):
    cart = Cart(request)

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()  # Order
            for obj in cart:
                OrderItemModel.objects.create(
                    order=order,
                    item=obj.get('item'),
                    price=obj.get('price'),
                    quantity=obj.get('quantity')
                )

            # clear cart
            cart.clear()
            return render(request, "", {"order": order}) # order successful
    else:
        form = OrderCreateForm()
    return render(request, "orders/create_order.html", {"cart": cart, "form": form})
