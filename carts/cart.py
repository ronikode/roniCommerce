"""

"""
from decimal import Decimal

from catalogue.models import ItemModel
from config import settings


class Cart:

    def __init__(self, request):
        """

        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)  # sessionID
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart  # -> {'cart': "ansdnakdnkq123", 'id_item'}

    def add(self, item: 'ItemModel', quantity=1, override_quantity=False):
        """
        Add a item to cart.
        """
        item_id = str(item.pk)
        self.cart[item_id] = {
            'quantity': 0, 'pvp': item.pvp
        }

        if override_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity

        self.save()

    def save(self):
        # save the session
        self.session.modified = True

    def remove(self, item: 'ItemModel'):
        """
        Remove a item from the cart.
        """
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items and get the items from the db.
        """
        item_ids = self.cart.keys()  # cart[2] -> Item (pk=2)
        # get the item objects that added to cart.
        items = ItemModel.objects.filter(id__in=item_ids)  # [2, 5, 6]
        temp = self.cart.copy()
        for item in items:
            temp[str(item.id)]['item'] = item  # {'id': [itemModel1, itemModel2]}

        for item in temp.values():  # dict() -> .values() -> [ItemModel1, ItemModel2, ItemModel3....]
            item['price'] = Decimal(item.get('pvp'))
            item['subtotal'] = item.get('pvp') * item.get('quantity')
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        # counter = 0
        # for item in self.cart.values():
        #     counter += item['quantity']
        return sum(item['quantity'] for item in self.cart.values())  # list comprehension

    def get_total(self):
        return sum(Decimal(item['quantity'] * item['pvp']) for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()
