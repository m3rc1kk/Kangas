from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Product
from orders.models import Order

def user_directory_path(instance, filename):
    return f'{instance.username}/profile_avatars/{filename}'

class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)
    city = models.CharField(max_length=30)
    favorites = models.ManyToManyField(Product, related_name='favorites', blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[self.id])