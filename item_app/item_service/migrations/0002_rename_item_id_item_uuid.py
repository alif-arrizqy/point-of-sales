# Generated by Django 4.2.4 on 2023-08-25 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='uuid',
        ),
    ]
