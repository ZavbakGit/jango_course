from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_of_week = {
    "monday": "Понедельник",
    "tuesday": "Вторник",
    "wednesday": "Среда",
    "thursday": "Четверг",
    "friday": "Пятница",
    "saturday": "Субота",
    "sunday": "Воскресенье",
}


def get_info_day_of_week(request, day):
    if day.lower() in days_of_week:
        return HttpResponse(days_of_week[day.lower()])
    return HttpResponseNotFound(f"Неизвестный день - {day}")


def get_info_day_of_week_by_number(request, day: int):
    if 0 < day <= len(days_of_week):
        name = list(days_of_week.keys())[day - 1]
        redirect_url = reverse('todo-week-name', args=[name])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неизвестный день - {day}")


def get_greeting(request):
    return render(request, 'week_days/greeting.html')
