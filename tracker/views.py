from django.shortcuts import render, redirect, get_object_or_404
from .models import User, BaseModel, Habit, DailyRecord
from django.contrib.auth.decorators import login_required, user_passes_test
#from .forms import HabitForm


def home(request):
    if request.user.is_authenticated:
        return redirect('list_habits')
    return render(request, 'tracker/home.html')


#@login_required
def list_habits(request):
    habit_list = Habit.objects.all()
    return render(request, 'tracker/list_habits.html',
                {"habit_list": habit_list})


