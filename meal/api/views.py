from meal.api.serializers import IngredientSerializer, MealIngredientsSerializer, MealSerializer
from meal.models import Ingredient, Meal, MealIngredients

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
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
    data = MealIngredients.objects.all()
    serializer = MealIngredientsSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def meal_create(request):
    data = request.data
    serializer = MealSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"meal created successfully",
            "data":serializer.data
        },status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ingredient_create(request):
    data=request.data
    serialier=IngredientSerializer(data=data)
    if serialier.is_valid():
        serialier.save()
        return Response({
            "message":"ingredient created successfully",
            "data":serialier.data
        }, status.HTTP_201_CREATED)
    else:
        return Response(serialier.errors,status.HTTP_400_BAD_REQUEST)

        