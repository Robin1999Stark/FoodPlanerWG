from django.db import models
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    profilepicture = models.ImageField(
        upload_to='profile_pictures/', null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class UnitOptions(models.TextChoices):
    KG = 'kg', 'KG'
    LITER = 'l', 'L'
    GRAM = 'g', 'G'
    MILLILITRE = 'ml', 'ML'
    PIECE = 'stk', 'stk.'
    TEASPOON = 'tsp', 'TSP'
    TABLESPOON = 'TBSP', 'Tbsp'
    OUNCE = 'oz'
    CUP = 'cup'
    GALLON = 'gal', 'gallon'
    PINCH = 'pinch', 'prise'
    DROP = 'drop', 'Tropfen'
    HANDFUL = 'handful'
    SPRIG = 'sprig', 'Zweig'
    CLOVE = 'Zehe', 'clove'
    SHEET = 'sheet', 'Blatt'
    BOTTLE = 'bottle', 'Flasche'
    BUNCH = 'bund', 'bunch'
    PACKAGE = 'Package', 'package'
    BAR = 'tafel', 'bar'
    CAN = 'can', 'dose'
    STICK = 'stick', 'stange'


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=200, unique=True)


class Ingredient(models.Model):
    title = models.CharField(max_length=180, primary_key=True, null=False)
    description = models.CharField(null=True, max_length=1200)
    preferedUnit = models.CharField(
        choices=UnitOptions.choices,
        null=True,
        default=UnitOptions.PIECE,
        max_length=20)


class IngredientTags(models.Model):
    ingredient = models.OneToOneField(
        Ingredient, blank=False, primary_key=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)


class Meal(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, max_length=500)
    ingredients = models.ManyToManyField(
        Ingredient, blank=True, through='MealIngredient')
    duration = models.PositiveSmallIntegerField(default=0)
    preparation = models.TextField(null=True, blank=True)
    portion_size = models.PositiveIntegerField(
        default=4, help_text="Portion size (number of servings)")
    picture = models.ImageField(upload_to='meal_pictures/', null=True,
                                blank=True, help_text="Upload a picture of the meal")


class MealTags(models.Model):
    meal = models.OneToOneField(
        Meal, blank=False, primary_key=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)


class MealIngredient(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name='meal_to_ingredient')
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='ingredient_to_meal')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10)

    class Meta:
        db_table = 'meal_ingredient'
        constraints = [
            models.UniqueConstraint(
                fields=['meal', 'ingredient'], name='unique_meal_ingredient')
        ]


class FoodPlanerItem(models.Model):
    date = models.DateField(primary_key=True, unique=True)
    meals = models.ManyToManyField(Meal, blank=True)


class InventoryItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    unit = models.CharField(
        max_length=20,
        choices=UnitOptions.choices,
        default=UnitOptions.PIECE,
    )


class ShoppingListItem(models.Model):
    bought = models.BooleanField(default=False)
    added = models.DateTimeField(default=timezone.now)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, default=1, decimal_places=2, null=True)
    unit = models.CharField(
        max_length=20,
        choices=UnitOptions.choices,
        default=UnitOptions.PIECE,
    )
    notes = models.TextField(
        blank=True,
        null=True,
        max_length=200,
    )


class ShoppingList(models.Model):
    created = models.DateTimeField(default=timezone.now)
    items = models.ManyToManyField(ShoppingListItem, blank=True)
