from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Min, Max, Avg, Count, Sum, Value


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_first=True))
    movies = Movie.objects.annotate(
        field_true=Value(True),
        field_false=Value(False),
        buget_100=F('budget') + 100,
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    # for movie in movies:
    #     movie.save()

    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_ont_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_directors(request):
    directors = Director.objects.all()

    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
    })


def show_one_director(request, id_dir: int):
    director = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/director_detail.html', {
        'director': director
    })


def show_actors(request):
    actors = Actor.objects.all()

    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })


def show_one_actor(request, id_actor: int):
    actor = get_object_or_404(Actor, id=id_actor)
    return render(request, 'movie_app/actor_detail.html', {
        'actor': actor
    })
