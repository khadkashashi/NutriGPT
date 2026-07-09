from rest_framework import serializers

from meal.models import Ingredient, Meal, MealIngredients


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"



class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class MealIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealIngredients
        fields = "__all__"