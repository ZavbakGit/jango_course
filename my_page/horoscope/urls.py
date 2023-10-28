from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MYFloatConverter, 'my_float')
register_converter(converters.MYDateConverter, 'my_date')

urlpatterns = [
    path('', views.index,name='horoscope-index'),
    path('<my_date:date>/', views.get_my_date_converters),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('type/', views.get_list_zodiac_type),
    path('type/<str:element_horoscope>', views.get_zodiac_type, name='horoscope-element'),
    path('<yyyy:digit>/', views.get_yyyy_converters),
    path('<int:sign>/', views.get_info_about_zodiac_sign_by_number),
    path('<my_float:digit>/', views.get_my_float_converters),
    path('<str:sign>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
]
