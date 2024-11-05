# Generated by Django 5.1.2 on 2024-11-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='products/%Y/%m/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['id', 'slug'], name='main_produc_id_f4bffc_idx'), models.Index(fields=['name'], name='main_produc_name_168fc5_idx'), models.Index(fields=['-created'], name='main_produc_created_4330ad_idx')],
            },
        ),
    ]