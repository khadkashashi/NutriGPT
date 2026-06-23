from django.contrib import admin

from .models import Ingredient, Meal, MealIngredients, MealPlan, MealPlanItems


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "start_date",
        "end_date",
        "generated_by_ai",
        "created_at",
    )
    list_filter = (
        "generated_by_ai",
        "start_date",
        "end_date",
        "created_at",
    )
    search_fields = (
        "title",
        "user__username",
        "user__email",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)



@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "meal_type",
        "prepare_time",
    )
    list_filter = ("meal_type",)
    search_fields = ("name",)


@admin.register(MealPlanItems)
class MealPlanItemsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "meal_plan",
        "meal",
        "date",
    )
    list_filter = (
        "date",
        "meal__meal_type",
    )
    search_fields = (
        "meal_plan__title",
        "meal__name",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "unit",
        "calories_per_100g",
        "protein_per_100g",
        "carbs_per_100g",
        "fat_per_100g",
    )
    search_fields = ("name",)


@admin.register(MealIngredients)
class MealIngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "meal",
        "ingredient",
        "quantity",
    )
    search_fields = (
        "meal__name",
        "ingredient__name",
    )