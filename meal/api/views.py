from meal.api.serializers import IngredientSerializer, MealIngredientsSerializer, MealSerializer
from meal.models import Ingredient, Meal, MealIngredients
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
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


@api_view(['PUT'])
def meal_update(request, id):
    meal=Meal.objects.get(id=id)
    data=request.data
    serializer=MealSerializer(meal,data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "mesaage":"meal update successfully"
        }, status.HTTP_200_OK )
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def meal_delete(request, id):
    meal = Meal.objects.filter(id=id)
    meal.delete()
    return Response({
        "message":"Meal Deleted Successfully"
    }, status.HTTP_204_NO_CONTENT)



class IngredientView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Ingredient
    serializer_class =IngredientSerializer


    def get(self, request):
        data = Ingredient.objects.all()
        serializer = IngredientSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Ingredient created successfully",
                "data":serializer.data
            },status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        


class IngredientAction(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Ingredient
    serializer_class =IngredientSerializer

    def get(self, request, id):
        data = Ingredient.objects.get(id=id)
        serializer = IngredientSerializer(data, many=False)
        #  data=self.get_object_or_400(Ingredient, id=id)
        return Response(serializer.data)

    def put(self, request, id):
        ingredient=Ingredient.objects.get(id=id)
      
        data=request.data
        serializer=IngredientSerializer(ingredient,data=data)
        if serializer.is_valid():
         serializer.save()
         return Response({
            "mesaage":"ingredient update successfully"
        }, status.HTTP_200_OK )
        else:
         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, id):
        ingredient = Ingredient.objects.filter(id=id)
        ingredient.delete()
        return Response({
        "message":"Meal Deleted Successfully"
    }, status.HTTP_204_NO_CONTENT)