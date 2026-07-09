from meal.api.serializers import IngredientSerializer, MealIngredientsSerializer, MealSerializer
from meal.models import Ingredient, Meal, MealIngredients

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def meal_list(request):
    data = Meal.objects.all()
    serializer = MealSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ingredient_list(request):
    data = Ingredient.objects.all()
    serializer = IngredientSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mealingredinet_list(request):
    data = MealIngredients
    serializer = MealIngredientsSerializer(data, many=True)
    return Response(serializer.data)