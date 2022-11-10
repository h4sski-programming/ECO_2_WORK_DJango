from datetime import date
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Activity
# from .forms import ActivityForm


def index(request):
    user = User.objects.get(id=2)
    users = User.objects.all()
    activity = Activity.objects.filter(user=user.id).order_by('-date')
    return render(request, 'eco2work_app/index.html', {
        'user': user,
        'users': users,
        'activity': activity,
    })


def profile(request):
    user = User.objects.get(id=2)
    activity = Activity.objects.filter(user=user.id).order_by('-date')
    return render(request, 'eco2work_app/profile.html', {
        'user': user,
        'activity': activity,
    })


def activity(request):
    today = date.today()
    user = User.objects.get(id=2)
    activity = Activity.objects.filter(user=user.id).order_by('-date')
    vehicle_list = activity.first().get_vehicles()
    return render(request, 'eco2work_app/activity.html', {
        'today': today,
        'user': user,
        'activity': activity,
        'vehicle_list': vehicle_list,
    })
