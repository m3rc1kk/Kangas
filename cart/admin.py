from django.contrib import admin

from cart.models import CartModel

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'size']
