from django.shortcuts import render
from meals.models import Meal, MealIngredients, MealPlan, MealPlanItems, Ingredient
from django.db.models import Count

# Create your views here.


def dashboard(request):
    meal = Meal.objects.all()
    meal_ingredient = MealIngredients.objects.all()
    meal_plan = MealPlan.objects.all()
    meal_plan_items = MealPlanItems.objects.all()
    ingredient = Ingredient.objects.all()
    meal_type = meal.values_list('meal_type').annotate(count = Count('meal_type')).order_by('meal_type')
    context = {
        "cards": [
            {"title": "Meals", "count": meal.count()},
            {"title": "Meal Ingredients", "count": meal_ingredient.count()},
            {"title": "Meal Plans", "count": meal_plan.count()},
            {"title":"Ingredient", "count":ingredient.count()},
        ],
        "meal_type":[{"title":i[0], "count":i[1]} for i in meal_type],
    }

    return render(request, "home/base.html", context)