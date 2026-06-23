from django.core.management.base import BaseCommand, CommandError
from meal.models import Meal
import random


class Command(BaseCommand):
    help = "Testing commands"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        meal_types = ["BreakFast", "Lunch", "Dinner", "Snacks"]

        for i in  range(1,400):
           Meal.objects.create(
               name = f"Meal {i}",
               meal_type =random.choice(meal_types),
               prepare_time =random.randint(50,100)
           )
        self.stdout.write(
            self.style.SUCCESS('Successfully Meal added')
            )