from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Min, Max, Avg, Count, Sum


def show_all_movie(request):
    movies = Movie.objects.order_by(F('year').desc(nulls_first=True))
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
