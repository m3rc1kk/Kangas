from decimal import Decimal
from django.conf import settings

from account.views import register
from main.models import Product
from .models import CartModel

class Cart:
    def __init__(self, user):
        self.user = user

    def add(self, product, quantity=1, override_quantity=False):
        cart_item = CartModel.objects.filter(user=self.user, product=product).first()

        if cart_item:
            if override_quantity:
                cart_item.quantity = quantity
            else:
                cart_item.quantity += quantity
            cart_item.save()
        else:
            CartModel.objects.create(user= self.user, product=product, quantity=quantity)

    def remove(self, product):
        CartModel.objects.filter(user=self.user, product=product).delete()

    def __iter__(self):
        cart_items = CartModel.objects.filter(user=self.user).select_related('product')
        for item in cart_items:
            yield {
                'product': item.product,
                'quantity': item.quantity,
                'price': item.product.price,
                'total_price': item.get_total_price(),
            }

    def __len__(self):
        return sum(item.quantity for item in CartModel.objects.filter(user=self.user))

    def get_total_price(self):
        return sum(item.get_total_price() for item in CartModel.objects.filter(user=self.user))

    def clear(self):
        CartModel.objects.filter(user=self.user).delete()