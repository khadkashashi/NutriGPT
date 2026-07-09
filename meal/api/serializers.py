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


# class MealIngredientsSerializer(serializers.ModelSerializer):
#     meal = MealSerializer(read_only=True)
#     ingredient = IngredientSerializer(read_only=True)
#     class Meta:
#         model = MealIngredients
#         fields = "__all__"


class MealIngredientsSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    
    class Meta:
        model = MealIngredients
        fields = "__all__"

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data['meal']=f'{instance.meal.name}-{instance.meal.meal_type}'
        return data