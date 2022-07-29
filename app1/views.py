from django.shortcuts import render

from app1.models import ModelFilm


def homepage(request):
    films = ModelFilm.objects.all()
    return render(request, 'app1/homepage.html',
                  {'films': films})


def movie_details(request, id):
    movie = ModelFilm.objects.get(id=id)
    return render(request, 'app1/movie_details.html',
                  {'movie': movie})
