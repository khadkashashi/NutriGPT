from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_mealplan")
    title = models.CharField(max_length=30, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    generated_by_ai = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        model = "meal_plan"