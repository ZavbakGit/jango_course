from django.shortcuts import render, get_object_or_404
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.all()
    # for movie in movies:
    #     movie.save()

    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_ont_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })
