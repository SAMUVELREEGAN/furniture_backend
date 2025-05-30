# Generated by Django 5.2 on 2025-05-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_pro_img_alter_product_star_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
