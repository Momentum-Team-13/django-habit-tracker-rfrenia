from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DailyRecord, Habit, User

admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(DailyRecord)