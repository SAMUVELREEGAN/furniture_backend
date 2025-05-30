# Generated by Django 5.1.2 on 2025-05-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proSize', '0004_alter_productsize_category_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productsize',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='sizes',
            field=models.CharField(help_text='Comma-separated list of sizes', max_length=100),
        ),
    ]
