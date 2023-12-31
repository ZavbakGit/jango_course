from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='geometry-rectangle'),
    path('square/<int:width>/', views.get_square_area, name='geometry-square'),
    path('circle/<int:radius>/', views.get_circle_area, name='geometry-circle'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.get_rectangle_area_redirect),
    path('get_square_area/<int:width>/', views.get_square_area_redirect),
    path('get_circle_area/<int:radius>/', views.get_circle_area_redirect),
]
