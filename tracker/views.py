from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, BaseModel, Habit, DailyRecord
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import HabitForm, DailyRecordForm



def home(request):
    if request.user.is_authenticated:
        return redirect('list_habits')
    return render(request, 'tracker/home.html')


@login_required
def list_habits(request):
    habit_list = Habit.objects.all()
    return render(request, 'tracker/list_habits.html',
                {"habit_list": habit_list})


@login_required
def habit_detail(request, pk):
    habits = Habit.objects.all()
    habit = get_object_or_404(habits, pk=pk)
    return render(request, "tracker/habit_detail.html",
        {"habit": habit})


# @login_required
# def add_entry(request):
#     if request.method == "POST":
#         form = DailyRecordForm(data=request.POST)
#         if form.is_valid():
#             habit = form.save(commit=False)
#             habit.user = request.user
#             habit.save()
#             messages.success(request, "Entry added!")
#             return redirect("habit_detail", pk=habit.pk)

#     else:
#         form = DailyRecordForm()

#     return render(request, "tracker/add_entry.html", {"form": form})


@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            messages.success(request, "Habit added!")
            return redirect("habit_detail", pk=habit.pk)

    else:
        form = HabitForm()

    return render(request, "tracker/add_habit.html", {"form": form})


@login_required
def delete_habit(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        habits.delete()
        return redirect(to="list_habits")
    return render(request, "tracker/delete_habit.html", 
                    {"habits": habits})


@login_required
def edit_habit(request, pk):
    habits = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        forms = HabitForm(instance=habits)

    else:
        forms = HabitForm(data=request.POST, instance=habits)
        if forms.is_valid():
            forms.save()
            return redirect(to="habit_detail")

    return render(request, "tracker/edit_habit.html", 
                    {"forms": forms, "habits": habits})


@login_required
def add_entry(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == "POST":
        form = DailyRecordForm(data=request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.habit = habit
            entry.save()

    return redirect("habit_detail", pk=habit.pk)