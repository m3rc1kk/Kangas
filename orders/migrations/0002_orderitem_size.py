# Generated by Django 5.1.2 on 2024-11-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
