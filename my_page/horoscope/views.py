from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from datetime import datetime as dt, datetime
from dataclasses import dataclass

signs_dictionary = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_type = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    'aries': [80, 110],
    'taurus': [111, 141],
    'gemini': [142, 172],
    'cancer': [173, 203],
    'leo': [204, 233],
    'virgo': [234, 266],
    'libra': [267, 296],
    'scorpio': [297, 326],
    'sagittarius': [327, 356],
    'capricorn': [357, 20],
    'aquarius': [21, 50],
    'pisces': [51, 79]
}


def get_yyyy_converters(request, digit: str):
    return HttpResponse(f'Вы передали чимло из 4-х числед - {digit}')


def get_my_date_converters(request, date: str):
    return HttpResponse(f'Вы передали дату - {date}')


def get_my_float_converters(request, digit: str):
    return HttpResponse(f'Вы передали вещественное чимло - {digit}')


def get_info_by_date(request, month: int, day: int):
    """Знак зодиака по дню """

    try:
        date = dt(datetime.now().year, month, day)
    except ValueError:
        return HttpResponseNotFound(f"Не правильная дата")

    num = date.timetuple().tm_yday
    for sign, dates in zodiac_dates.items():
        if num in range(dates[0], dates[1]):
            redirect_url = reverse("horoscope-name", args=[sign])
            return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Не правильная дата")


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}, age {self.age}'


def get_info_about_zodiac_sign(request, sign: str):
    description = signs_dictionary.get(sign, None)

    for i, k in signs_dictionary.items():
        print(k)

    data = {
        'description': description,
        'sign': sign,
        'zodiacs': signs_dictionary,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_sign_by_number(request, sign: int):
    if 0 < sign <= len(signs_dictionary):
        name_zodiac = list(signs_dictionary.keys())[sign - 1]
        redirect_url = reverse("horoscope-name", args=[name_zodiac])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неправельный номер - {sign}")


def get_list_zodiac_type(request):
    """Меню  стихий"""

    list_type = list(zodiac_type)

    li_elements = ''
    for elem in list_type:
        redirect_url = reverse("horoscope-element", args=[elem])
        li_elements += f"<li><a href='{redirect_url}'>{elem.title()}</a></li>"

    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


def get_zodiac_type(request, element_horoscope: str):
    """Выводит список знаков входящих в стихию"""

    # Список знаков входящих в стихию
    list_item = zodiac_type.get(element_horoscope, None)
    if list_item:
        li_elements = ''
        for elem in list_item:
            redirect_url = reverse("horoscope-name", args=[elem])
            li_elements += f"<li><a href='{redirect_url}'>{elem.title()}</a></li>"

        response = f"""
           <H2>{element_horoscope.title()}</H2>
           <ol>
               {li_elements}
           </ol>
           """
        return HttpResponse(response)

    else:
        return HttpResponseNotFound(f"Неизвестная стихия - {element_horoscope}")


def index(request):
    data = {
        'zodiacs': list(signs_dictionary)
    }
    return render(request, 'horoscope/index.html', context=data)
