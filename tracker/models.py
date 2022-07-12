from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    #user_name = models.CharField(max_length=255, null=True, blank=True)
    #email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Habit(models.Model):
    habit_name = models.CharField(max_length=255)
    target = models.IntegerField(max_length=255) 
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    unit = models.CharField(max_length=255)
    #note = models.TextField(null=True, blank=True)


class DailyRecord(models.Model):
    note = models.TextField(null=True, blank=True)
    note_time = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    action_number = models.IntegerField(null=True, blank=True,)
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE, null=True, blank=True)
