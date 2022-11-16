from datetime import date, datetime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import Activity
from .forms import TestingForm


def sum_activity_distance(user_id=None, y=None, m=None):
    if user_id:
        activities = Activity.objects.filter(user=user_id).all()
    else:
        activities = Activity.objects.all()

    sum = 0
    d1 = date(year=y, month=m, day=1)
    d2 = date(year=y, month=m+1, day=1)
    for a in activities:
        if d1 <= a.date < d2:
            sum = sum + a.distance
    return sum


def index(response):
    user = response.user
    if not user.is_authenticated:
        return redirect('/login')
    users = User.objects.all()
    activity = Activity.objects.all().order_by('-date')
    return render(response, 'eco2work_app/index.html', {
        'user': user,
        'users': users,
        'activity': activity,
    })


def profile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('/login')
    activity = Activity.objects.filter(user=user.id).order_by('-date')
    vehicle_list = Activity.objects.first().get_vehicles()

    form = TestingForm()

    today = date.today()
    sum_distance = sum_activity_distance(
        user_id=user.id, y=today.year, m=today.month)
    return render(request, 'eco2work_app/profile.html', {
        'today': today,
        'user': user,
        'activity': activity,
        'vehicle_list': vehicle_list,
        'sum_distance': sum_distance,
        'form': form,
    })


def activity(response):
    user = response.user
    if not user.is_authenticated:
        return redirect('/login')

    def get_activity(act_id):
        return Activity.objects.get(id=act_id)

    def get_atributes():
        distance = response.POST.get('distance')
        vehicle = response.POST.get('vehicle')
        return [distance, vehicle]

    def get_date_from_string(s):
        y, m, d = s.split('-')
        return date(year=int(y), month=int(m), day=int(d))

    if response.method == 'POST':
        if response.POST.get('new_activity'):
            d = get_date_from_string(response.POST.get('date'))
            if not (d in Activity.objects.filter(user=user).values_list('date', flat=True)):
                distance, vehicle = get_atributes()
                activity_temp = Activity()
                activity_temp.user = user
                activity_temp.date = d
                activity_temp.distance = distance
                activity_temp.vehicle = vehicle
                activity_temp.save()
            else:
                print(f'Date already has activity, please edit it.')

        elif response.POST.get('delete'):
            activity_id = response.POST.get('delete')
            get_activity(activity_id).delete()

        elif response.POST.get('update'):
            activity_id = response.POST.get('update')
            activity_to_edit = get_activity(activity_id)
            distance, vehicle = get_atributes()
            activity_to_edit.distance = distance
            activity_to_edit.vehicle = vehicle
            activity_to_edit.save()
        else:
            print(
                f'Incorrect form POST action, not [new_activity, update, delete].')

    today = date.today()
    month_start = today.replace(day=1)
    next_month = month_start.replace(
        month=month_start.month + 1)
    month_end = next_month - datetime.timedelta(days=1)

    sum_distance = sum_activity_distance(
        user_id=user.id, y=today.year, m=today.month)
    activity = Activity.objects.filter(user=user.id).order_by('-date')
    vehicle_list = Activity.objects.first().get_vehicles()

    return render(response, 'eco2work_app/activity.html', {
        'today': today,
        'month_start': month_start,
        'month_end': month_end,
        'user': user,
        'activity': activity,
        'vehicle_list': vehicle_list,
        'sum_distance': sum_distance,
    })
