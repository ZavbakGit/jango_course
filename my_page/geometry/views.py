from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    # geometry/rectangle/5/6
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    # geometry/square/10
    # return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    # geometry/circle/6
    # return HttpResponse(f'Площадь круга радиуса {radius} равна {radius * 3, 14}')
    return render(request, 'geometry/circle.html')


def get_rectangle_area_redirect(request, width: int, height: int):
    redirect_url = reverse('geometry-rectangle', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def get_square_area_redirect(request, width: int):
    redirect_url = reverse('geometry-square', args=[width])
    return HttpResponseRedirect(redirect_url)


def get_circle_area_redirect(request, radius: int):
    redirect_url = reverse('geometry-circle', args=[radius])
    return HttpResponseRedirect(redirect_url)
