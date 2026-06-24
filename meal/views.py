from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from meal.models import Meal
from meal.forms import MealForm

class MealView(ListView):
    model = Meal
    template_name = 'meal/index.html'
    context_object_name = 'meal'

class MealCreateView(CreateView):
    model = Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url = '/meal'

class MealUpdateView(UpdateView):   
    model = Meal
    template_name = 'meal/create.html'
    form_class = MealForm
    success_url = '/meal'
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from meal.models import Meal
from meal.forms import MealForm
# Create your views here.


class MealView(ListView):
    model = Meal
    paginate_by = 10
    template_name = 'meal/index.html'
    context_object_name = 'meal'


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
class MealDeleteView(DeleteView):   
    model = Meal
    success_url = '/meal'