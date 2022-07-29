from django.shortcuts import render

from app1.models import ModelFilm


def homepage(request):
    film = ModelFilm.objects.all()
    return render(request, 'app1/homepage.html',
                  {'film': film})
