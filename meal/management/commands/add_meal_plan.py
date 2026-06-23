from django.core.management.base import BaseCommand, CommandError
from meal.models import Meal, MealPlan
import random
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):
    help = "Add Meal plan"

    # def add_arguments(self, parser):
    #     parser.add_argument("poll_ids", nargs="+", type=int)
    fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.all().values_list('id')
        n = 340
        for i in range(1,n):
            MealPlan.objects.create(
                user_id = random.choice(user)[0],
                start_date= self.fake.date_between(start_date='-10y', end_date='today'),
                end_date = self.fake.date_between(start_date='-10y', end_date='today')

            )
            self.stdout.write(self.style.SUCCESS(f'{i}/{n-1} number completed'))