"""

"""

from django.urls import path

from carts.views import cart_add, cart_remove, cart_detail

app_name = "carts"
urlpatterns = [

    path('add/<int:item_id>', cart_add, name="cart_add"),
    path('remove/<int:item_id>', cart_remove, name="cart_remove"),
    path('detail/', cart_detail, name="cart_detail")

]
