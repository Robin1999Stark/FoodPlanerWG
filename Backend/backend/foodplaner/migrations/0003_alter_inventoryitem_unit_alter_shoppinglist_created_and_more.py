# Generated by Django 4.2.3 on 2023-12-05 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplaner', '0002_shoppinglistitem_shoppinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='unit',
            field=models.CharField(choices=[('kg', 'KG'), ('l', 'L'), ('g', 'G'), ('ml', 'ML'), ('stk', 'stk.'), ('tsp', 'TSP'), ('TBSP', 'Tbsp'), ('oz', 'Ounce'), ('cup', 'Cup'), ('gal', 'gallon'), ('pinch', 'prise'), ('drop', 'Tropfen'), ('handful', 'Handful'), ('sprig', 'Zweig'), ('Zehe', 'clove'), ('sheet', 'Blatt'), ('bottle', 'Flasche'), ('bund', 'bunch'), ('Package', 'package')], default='stk', max_length=20),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 15, 41, 7, 222905)),
        ),
        migrations.AlterField(
            model_name='shoppinglistitem',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 15, 41, 7, 222905)),
        ),
    ]
