from django.shortcuts import render, redirect, get_object_or_404
from .models import User, BaseModel, Habit, DailyRecord
#from .forms import HabitForm


def home(request):
    habit_list = Habit.objects.all()
    # if request.user.is_authenticated:
    #     return redirect('list_habits')
    return render(request, 'tracker/home.html', {"habit_list": habit_list})


# def list_habits(request):
#     habit_list = Habit.objects.all()
#     return render(request, 'tracker/home.html',
#                 {"habit_list": habit_list})
