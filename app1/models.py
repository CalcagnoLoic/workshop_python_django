from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelFilm(models.Model):
    class LandChoices(models.TextChoices):
        Belgique = "BE",
        France = "Fr",
        Allemagne = "DE",
        Italie = "IT"

    name = models.CharField(max_length=200)
    year = models.IntegerField(validators=[
        MinValueValidator(1950), MaxValueValidator(2022)])
    author = models.CharField(max_length=100)
    english = models.BooleanField(default=False)
    land_production = models.CharField(choices=LandChoices.choices, max_length=25)
    official_page = models.CharField(max_length=150)
