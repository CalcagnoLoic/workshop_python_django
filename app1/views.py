from django.shortcuts import render, redirect

from app1.forms import AddFilm
from app1.models import ModelFilm


def homepage(request):
    films = ModelFilm.objects.all()
    return render(request, 'app1/homepage.html',
                  {'films': films})


def movie_details(request, id):
    movie = ModelFilm.objects.get(id=id)
    return render(request, 'app1/movie_details.html',
                  {'movie': movie})


def add_movies(request):
    if request.method == "POST":
        form = AddFilm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_details', movie.id)
    else:
        form = AddFilm()

    return render(request, 'app1/add_film.html',
                  {'form': form})
