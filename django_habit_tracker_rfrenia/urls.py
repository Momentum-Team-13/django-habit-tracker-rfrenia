"""django_habit_tracker_rfrenia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
import debug_toolbar
from tracker import views as tracker_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registration.backends.simple.urls')),
    path('', tracker_views.home, name='home'),
    path('habits/', tracker_views.list_habits, name='list_habits'),
    path('habits/new', tracker_views.add_habit, name='add_habit'),
    path('tracker/<int:habit_pk>/entry', tracker_views.add_entry, name='add_entry'),
    path('tracker/<int:pk>', tracker_views.habit_detail, name='habit_detail'),
    path('tracker/<int:pk>/edit', tracker_views.edit_habit, name='edit_habit'),
    path('tracker/<int:pk>/delete', tracker_views.delete_habit, name='delete_habit'),
]
if settings.DEBUG:
    urlpatterns.append(path(r'__debug__/', include(debug_toolbar.urls)))