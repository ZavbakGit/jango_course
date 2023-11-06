from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_ont_movie, name='movie-detail'),
    path('directors', views.show_directors),
    path('directors/<int:id_dir>', views.show_one_director, name='director-detail'),
    path('actors', views.show_actors),
    path('actors/<int:id_actor>', views.show_one_actor, name='actor-detail'),
]
