# Generated by Django 5.2 on 2025-04-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
