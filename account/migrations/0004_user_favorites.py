# Generated by Django 5.1.2 on 2024-11-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_city'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='main.product'),
        ),
    ]
