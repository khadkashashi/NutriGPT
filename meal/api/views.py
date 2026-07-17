from meal.api.serializers import IngredientSerializer, MealIngredientsSerializer, MealSerializer,MealPlanSerializer
from meal.models import Ingredient, Meal, MealIngredients, MealPlan
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from meal.service import generate_json_data
import json
from meal.tasks import hello


@api_view(['GET'])
def meal_list(request):
    data = Meal.objects.all()
    serializer = MealSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def meal_plan(request):
    data=MealPlan.obecta.all()
    serializer= MealPlanSerializer(data,many=True)
    return Response(serializer.data)

@extend_schema(tags=["Ingredient-Func"], deprecated=True,summary="get all list of ingredient")
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
def MealPlan_create(request):
    data=request.data
    serializer=MealPlanSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"meaplplan creates sucess",
            "data": serializer.data
        }, status.HTTP_201_CREATED)
    else:
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


@extend_schema(tags=["Ingredient"])

class IngredientView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Ingredient
    serializer_class =IngredientSerializer

    @extend_schema(tags=["Ingredient"])
    def get(self, request):
        data = Ingredient.objects.all()
        serializer = IngredientSerializer(data, many=True)
        return Response(serializer.data)
    
    @extend_schema(tags=["Ingredient"])
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
    permission_classes = [IsAuthenticated]
    queryset = Ingredient
    serializer_class = IngredientSerializer

    @extend_schema(tags=["Ingredient"])
    def get(self, request, id):
        # data = Ingredient.objects.get(id=id)
        data = get_object_or_404(Ingredient, id=id)
        serializer = IngredientSerializer(data, many=False)
        return Response(serializer.data)

    @extend_schema(
        tags=["Ingredient"],
        summary="Udpdate required field ",
        description="this is put request for updating ingreient",
    )
    def put(self, request, id):
        pass

    def put(self, request, id):
        data = get_object_or_404(Ingredient, id=id)
        serializer = self.get_serializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Ingredient updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = get_object_or_404(Ingredient, id=id)
        data.delete()
        return Response(
            {"message": "Ingredient deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    @extend_schema(tags=["Ingredient"])
    def delete(self, request, id):
        pass


class MealPlanView(GenericAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def get(self, request):
        data = MealPlan.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Meal plan created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealPlanAction(GenericAPIView):
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def get(self, request, id):
        data = get_object_or_404(MealPlan, id=id)
        serializer = self.get_serializer(data, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(Meal, id=id)
        serializer = self.get_serializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Meal updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        data = get_object_or_404(Meal, id=id)
        data.delete()
        return Response(
            {"message": "Meal Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )


@extend_schema(tags=["AI"])
@api_view(["GET"])
def generate_nutri_ai(request):
    return Response({"ai_data": json.loads(generate_json_data())})