# Generated by Django 4.2.7 on 2023-11-27 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodplaner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('title', models.CharField(max_length=180, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='foodplaneritem',
            name='meals',
            field=models.ManyToManyField(blank=True, to='foodplaner.meal'),
        ),
        migrations.CreateModel(
            name='MealIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.ingredient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.meal')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ingredients', models.ManyToManyField(blank=True, through='foodplaner.InventoryItem', to='foodplaner.ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='inventory_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.inventorylist'),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(blank=True, through='foodplaner.MealIngredient', to='foodplaner.ingredient'),
        ),
    ]
