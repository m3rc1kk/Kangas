# Generated by Django 5.1.2 on 2024-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_current_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
