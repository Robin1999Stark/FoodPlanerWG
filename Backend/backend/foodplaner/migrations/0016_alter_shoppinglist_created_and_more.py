# Generated by Django 5.0 on 2023-12-21 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplaner', '0015_tag_alter_shoppinglist_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 23, 2, 50, 26288)),
        ),
        migrations.AlterField(
            model_name='shoppinglistitem',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 23, 2, 50, 25288)),
        ),
    ]
