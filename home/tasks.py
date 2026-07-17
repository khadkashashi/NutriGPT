from meal.models import MealIngredients, MealType
import random
from home.models import TodayMeal
from datetime import date


def get_breakfast_item():
    meal= MealIngredients.objects.filter(meal__meal_type=MealType.BREAKFAST)
    random_meal =random.choice(meal)
    today_meal=TodayMeal.object.create(
        date=str(date.today()),
        meal_ingredient=random_meal
    )



def get_snack_item():
    pass


def get_dinner_item():
    pass


def get_lunch_iterm():
    pass