# Generated by Django 5.1.2 on 2025-05-14 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_pro_name_alter_product_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='size',
            new_name='size_group',
        ),
        migrations.AddField(
            model_name='product',
            name='selected_size',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
