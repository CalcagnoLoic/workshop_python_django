from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelFilm(models.Model):
    class GenreChoices(models.TextChoices):
        Horreur = "H",
        Science_fiction = "SF",
        Comedie = "C",
        Drame = "D",
        Aventure = "A",
        Manga = "M",
        Thriller = "TH",
        Documentaire = "Doc"

    name = models.CharField(max_length=200)
    year = models.IntegerField(validators=[
        MinValueValidator(1950), MaxValueValidator(2022)])
    author = models.CharField(max_length=100)
    seen_or_not = models.BooleanField(default=False)
    genre = models.CharField(choices=GenreChoices.choices, max_length=25)
    official_page = models.CharField(max_length=150)
