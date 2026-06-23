from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MealType(models.TextChoices):
    BREAKFAST = "BreakFast"
    LUNCH = "Lunch"
    SNACKS = "Snacks"
    DINNER = "Dinner"


class MealPlan(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_mealplan"
    )
    title = models.CharField(max_length=30, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    generated_by_ai = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "meal_plan"


class Meal(models.Model):
    name = models.CharField(max_length=30)
    meal_type = models.CharField(max_length=20, choices=MealType.choices)
    description = models.TextField(null=True, blank=True)
    prepare_time = models.IntegerField(help_text="Enter time in minute")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meal"


class MealPlanItems(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.meal_plan.title}"

    class Meta:
        db_table = "meal_plan_items"


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=20, null=True, blank=True)
    calories_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    protein_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    carbs_per_100g = models.DecimalField(max_digits=5, decimal_places=2)
    fat_per_100g = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ingredient"


class MealIngredients(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.meal}"

    class Meta:
        db_table = "meal_ingredient"
        unique_together = ['meal','ingredient']