from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Habit(BaseModel):
    habit_name = models.CharField(max_length=255)
    target = models.IntegerField(null=True, blank=True,)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True, related_name="habits")
    unit = models.CharField(max_length=255, null=True, blank=True)
    #note = models.TextField(null=True, blank=True)


class DailyRecord(BaseModel):
    note = models.TextField(null=True, blank=True)
    #date is the daily time stamp of the entry
    #date = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    #action_number is the amount or quantity that the user did of their habit. Ex: 1000 steps taken
    action_number = models.IntegerField(null=True, blank=True,)
    habit = models.ForeignKey("Habit", on_delete=models.CASCADE, null=True, blank=True, related_name="dailyrecords")

    class meta:
        constaints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_entry')
        ]
