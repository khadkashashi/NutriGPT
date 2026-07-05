from django.urls import path
from meal.api.views import meal_list

urlpatterns = [
    path('', meal_list)
]