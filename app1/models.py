from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ModelPerson(models.Model):
    class LandChoices(models.TextChoices):
        Belgique = "BE",
        France = "Fr",
        Allemagne = "DE",
        Italie = "IT"

    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(100)])
    email = models.EmailField()
    english = models.BooleanField(default=False)
    land = models.CharField(choices=LandChoices.choices, max_length=25)
