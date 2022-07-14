from django import forms
from .models import User, Habit, BaseModel, DailyRecord


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'habit_name',
            'target',
            'unit',
        ]


class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = [
            'note',
            'action_number',
            'habit',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_name',
            'email',
        ]