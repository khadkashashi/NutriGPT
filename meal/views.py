from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from meal.models import Meal , Ingredient
from meal.forms import MealForm, IngredientForm
from meal.models import Meal, MealPlan
from meal.forms import MealForm, MealPlanForm
from meal.service import generate_json_data
import json # Create your views here.

#-------------------- Meal view --------------------

class MealView(ListView):
    model = Meal
    paginate_by = 10
    template_name = 'meal/index.html'
    context_object_name = 'meal'
    ordering = 'meal_type'



class MealCreateView(CreateView):
    model=Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url = '/meal'


class MealUpdateView(UpdateView):
    model=Meal
    template_name = 'meal/update.html'
    form_class = MealForm
    success_url = '/meal'


class MealDeleteView(DeleteView):
    model=Meal
    success_url = '/meal'

class IngredientListView(ListView):
    model = Ingredient
    paginate_by = 10
    template_name = "ingredient/ingredient_list.html"


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredients_create.html"
    success_url = "/meal/ingredients/"


class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "ingredient/ingredients_update.html"
    success_url = "/meal/ingredients/"


class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "ingredient/ingredients_delete.html"
    success_url = "/meal/ingredients/"


#-------------------- Meal Plane view --------------------

class MealPlanView(ListView):
    model = MealPlan
    paginate_by = 10
    template_name = 'mealPlan/index.html'
    context_object_name = 'mealPlan'


class MealPlanCreateView(CreateView):
    model=MealPlan
    template_name = 'mealPlan/create.html'
    form_class = MealPlanForm
    success_url = '/meal/plan/list'


class MealPlanUpdateView(UpdateView):
    model=MealPlan
    template_name = 'mealPlan/update.html'
    form_class = MealPlanForm
    success_url = '/meal/plan/list'


class MealPlanDeleteView(DeleteView):
    model = MealPlan
    template_name = 'mealPlan/delete.html'
    success_url = '/meal/plan/list'





def generate_ai_data(request):
    data = generate_json_data()
    data2 = json.loads(data)
    return render(request,'ingredient/ai.html', context={"data":data2})


def create_ai_ingredients(request, *args, **kwargs):
    data = kwargs.get('data')

    for i in data:
        print(i)
        # Ingredient.objects.create(**i)
    return redirect('meal/ingredients/')