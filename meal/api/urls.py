from django.urls import path
from meal.api.views import ingredient_list, meal_list, mealingredinet_list, meal_create

urlpatterns = [
    path('', meal_list),
    path('ingredient/', ingredient_list, name="ingredient-list"),
    path('mealingredinet/', mealingredinet_list, name="mealingredinet-list"),
    path('meal-create',meal_create)

]