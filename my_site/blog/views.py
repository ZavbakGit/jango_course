from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def main(request):
    # return HttpResponse("Главная страница")
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_info_about_post(request, name_post):
    # posts/лорлрло
    return HttpResponse(f"Информация о посте с именем {name_post}")


def get_info_about_by_number(request, number_post: int):
    # posts/5
    return HttpResponse(f"Информация о посте под номером {number_post}")
