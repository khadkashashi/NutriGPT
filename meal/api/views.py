from meal.api.serializers import MealSerializer
from meal.models import Meal

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def meal_list(request):
    data = Meal.objects.all()
    serializer = MealSerializer(data, many=True)
    return Response(serializer.data)