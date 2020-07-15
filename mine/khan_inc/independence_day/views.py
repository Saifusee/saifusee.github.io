from django.shortcuts import render
import datetime


def independence(request):
    aug = datetime.datetime.now()
    return render(request, "independence_day/august.html",{
        "I": aug.day == 15 and aug.month == 8
    })


def today(request):
    now = datetime.datetime.now()
    return render(request, "independence_day/today.html",{
        "a_day": now.day, "a_month": now.month, "a_year": now.year, "a_time": now.time
    })

# Create your views here.
