# Generated by Django 5.2 on 2025-04-25 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Logo', '0003_logo_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='product_image',
        ),
    ]
