from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('posts/', views.posts),
    path('posts/<int:number_post>/', views.get_info_about_by_number),
    path('posts/<str:name_post>/', views.get_info_about_post),

]