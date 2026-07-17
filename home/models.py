from django.db import models
from meal.models import MealIngredients

# Create your models here.
class TodayMeal(models.Model):
    date=models.DateField
    meal_ingredient =models.ForeignKey(MealIngredients, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meal_ingredient.meal.meal_type}-{self.date}'
