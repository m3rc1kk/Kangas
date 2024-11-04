from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return f'{instance.username}/profile_avatars/{filename}'

class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, blank=True)
    city = models.CharField(max_length=30)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username