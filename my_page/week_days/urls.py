from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_greeting),
    path('<int:day>/', views.get_info_day_of_week_by_number),
    path('<str:day>/', views.get_info_day_of_week, name='todo-week-name'),
]
