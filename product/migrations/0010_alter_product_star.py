# Generated by Django 5.1.2 on 2025-05-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_selected_size_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
