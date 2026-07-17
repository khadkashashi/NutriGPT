from django.contrib import admin
from home.models import TodayMeal
# Register your models here.
@admin.register(TodayMeal)
class TodayMealAdmin(admin.ModelAdmin):
    list_display=(
        "date",
        "meal_ingredient",
        "meal_ingredient__ingredient__name"


    )
    date_hierarchy = "date"
    autocomplete_fields = ['meal_ingredient']
    ordering = ("-date",)