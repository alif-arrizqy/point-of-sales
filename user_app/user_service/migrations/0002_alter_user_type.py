# Generated by Django 3.2.15 on 2023-08-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('regular', 'Regular'), ('vip', 'VIP'), ('wholesale', 'Wholesale')], default='reguler', max_length=10),
        ),
    ]
