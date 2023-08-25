# Generated by Django 4.2.4 on 2023-08-25 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0003_rename_uuid_user_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='uuid',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
