# Generated by Django 4.2.7 on 2023-11-22 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplaner', '0002_ingredient_meal_description_meal_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodplaneritem',
            name='meals',
            field=models.ManyToManyField(blank=True, to='foodplaner.meal'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='foodplaner.ingredient'),
        ),
    ]