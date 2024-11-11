from django.urls import reverse

from django.db import models


class Product(models.Model):
    class Sizes(models.TextChoices):
        S = 'S'
        M = 'M'
        L = 'L'
        XL = 'XL'
        XXL = 'XXL'


    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=3, choices=Sizes.choices, default = Sizes.S)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-detail', args = [self.id, self.slug])