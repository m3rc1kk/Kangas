from django.db import models
from django.conf import settings
from main.models import Product

class CartModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.user}"

    def get_total_price(self):
        return self.product.price * self.quantity