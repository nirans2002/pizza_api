# Generated by Django 4.0.5 on 2022-08-07 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='order_status',
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
