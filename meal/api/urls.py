from django.urls import path
from meal.api.views import ingredient_list, meal_list, mealingredinet_list, meal_create, ingredient_create, meal_delete, meal_update

urlpatterns = [
    path('', meal_list),
    path('ingredient/', ingredient_list, name="ingredient-list"),
    path('mealingredinet/', mealingredinet_list, name="mealingredinet-list"),
    path('meal-create',meal_create),
    path('ingredient-create', ingredient_create),
    path('meal-update/<int:id>', meal_update),
    path('meal-delete/<int:id>', meal_delete),

]