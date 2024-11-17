from email.policy import default

from django.conf import settings
from django.db import models
from main.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', null = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, null = True)

    class Meta:
        db_table = 'OrderItems'
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'


    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
