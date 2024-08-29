# Generated by Django 5.1 on 2024-08-29 13:13

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('title', models.CharField(max_length=180, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1200, null=True)),
                ('preferedUnit', models.CharField(choices=[('kg', 'KG'), ('l', 'L'), ('g', 'G'), ('ml', 'ML'), ('stk', 'stk.'), ('tsp', 'TSP'), ('TBSP', 'Tbsp'), ('oz', 'Ounce'), ('cup', 'Cup'), ('gal', 'gallon'), ('pinch', 'prise'), ('drop', 'Tropfen'), ('handful', 'Handful'), ('sprig', 'Zweig'), ('Zehe', 'clove'), ('sheet', 'Blatt'), ('bottle', 'Flasche'), ('bund', 'bunch'), ('Package', 'package'), ('tafel', 'bar'), ('can', 'dose'), ('stick', 'stange')], default='stk', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('description', models.TextField(max_length=500, null=True)),
                ('duration', models.PositiveSmallIntegerField(default=0)),
                ('preparation', models.TextField(blank=True, null=True)),
                ('portion_size', models.PositiveIntegerField(default=4, help_text='Portion size (number of servings)')),
                ('picture', models.ImageField(blank=True, help_text='Upload a picture of the meal', null=True, upload_to='meal_pictures/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profilepicture', models.ImageField(null=True, upload_to='profile_pictures/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_permissions_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('unit', models.CharField(choices=[('kg', 'KG'), ('l', 'L'), ('g', 'G'), ('ml', 'ML'), ('stk', 'stk.'), ('tsp', 'TSP'), ('TBSP', 'Tbsp'), ('oz', 'Ounce'), ('cup', 'Cup'), ('gal', 'gallon'), ('pinch', 'prise'), ('drop', 'Tropfen'), ('handful', 'Handful'), ('sprig', 'Zweig'), ('Zehe', 'clove'), ('sheet', 'Blatt'), ('bottle', 'Flasche'), ('bund', 'bunch'), ('Package', 'package'), ('tafel', 'bar'), ('can', 'dose'), ('stick', 'stange')], default='stk', max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='FoodPlanerItem',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False, unique=True)),
                ('meals', models.ManyToManyField(blank=True, to='foodplaner.meal')),
            ],
        ),
        migrations.CreateModel(
            name='MealIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=10)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_to_meal', to='foodplaner.ingredient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_to_ingredient', to='foodplaner.meal')),
            ],
            options={
                'db_table': 'meal_ingredient',
            },
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(blank=True, through='foodplaner.MealIngredient', to='foodplaner.ingredient'),
        ),
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought', models.BooleanField(default=False)),
                ('added', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, default=1, max_digits=10, null=True)),
                ('unit', models.CharField(choices=[('kg', 'KG'), ('l', 'L'), ('g', 'G'), ('ml', 'ML'), ('stk', 'stk.'), ('tsp', 'TSP'), ('TBSP', 'Tbsp'), ('oz', 'Ounce'), ('cup', 'Cup'), ('gal', 'gallon'), ('pinch', 'prise'), ('drop', 'Tropfen'), ('handful', 'Handful'), ('sprig', 'Zweig'), ('Zehe', 'clove'), ('sheet', 'Blatt'), ('bottle', 'Flasche'), ('bund', 'bunch'), ('Package', 'package'), ('tafel', 'bar'), ('can', 'dose'), ('stick', 'stange')], default='stk', max_length=20)),
                ('notes', models.TextField(blank=True, max_length=200, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodplaner.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('items', models.ManyToManyField(blank=True, to='foodplaner.shoppinglistitem')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientTags',
            fields=[
                ('ingredient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='foodplaner.ingredient')),
                ('tags', models.ManyToManyField(blank=True, to='foodplaner.tag')),
            ],
        ),
        migrations.CreateModel(
            name='MealTags',
            fields=[
                ('meal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='foodplaner.meal')),
                ('tags', models.ManyToManyField(blank=True, to='foodplaner.tag')),
            ],
        ),
        migrations.AddConstraint(
            model_name='mealingredient',
            constraint=models.UniqueConstraint(fields=('meal', 'ingredient'), name='unique_meal_ingredient'),
        ),
    ]
